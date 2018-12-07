using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Google.Cloud.Vision.V1;
using Microsoft.Win32;
using System.Security.Permissions;
using MongoDB.Driver;
using MongoDB.Bson;
using System.Collections;

namespace API_App
{
    public partial class Form1 : Form
    {

        ScriptEngine engine = Python.CreateEngine();
        dynamic stream_module; // streamer module
        dynamic stream; // streamer handle
        int tweet_count = 0;

        public Form1()
        {
            InitializeComponent();

            // to add to the search paths
            var searchPaths = engine.GetSearchPaths();
            string current_path = System.IO.Path.GetDirectoryName(Application.StartupPath);
            searchPaths.Add(@"..\..");

            // Add local IronPython Library to search path
            string exeFile = (new System.Uri(Assembly.GetEntryAssembly().CodeBase)).AbsolutePath;
            string exeDir = Path.GetDirectoryName(exeFile);
            searchPaths.Add(@"D:\software\IronPython\Lib\site-packages");   // site packages
            searchPaths.Add(@"D:\software\IronPython\Lib");                 // built-in packages
            engine.SetSearchPaths(searchPaths);

            // import the module
            dynamic hello_module = engine.ImportModule("hello");
            stream_module = engine.ImportModule("streamer");

            // execute hello funtion and display in Label
            debug.Text = stream_module.hello();

            // Instantiate a streamer
            string twitter_account = accont_tb.Text;
            var streamer = stream_module.stream(twitter_account);
            stream = streamer.streamImage();

            //twitter_pb.SizeMode = PictureBoxSizeMode.StretchImage;

            // initialize google vision key
            init_google_confidential();

            init_proxy_setting();

            initial_read_mongo();  // mongodb test
            update_mongo_dataview();
            update_stats_dataview();
        }

        private void init_google_confidential()
        {
            string variableName = "GOOGLE_APPLICATION_CREDENTIALS";
            string value = @"D:\keys\google\ec601-pp1-7e4843f1ee33.json";

            Environment.SetEnvironmentVariable(
            variableName,
            value,
            EnvironmentVariableTarget.Process
            );
           
        }

        private void init_proxy_setting()
        {
            var proxy = System.Net.HttpWebRequest.GetSystemWebProxy();

            //gets the proxy uri, will only work if the request needs to go via the proxy 
            //(i.e. the requested url isn't in the bypass list, etc)
            Uri proxyUri = proxy.GetProxy(new Uri("http://www.google.com"));

            Environment.SetEnvironmentVariable("http_proxy", proxyUri.AbsoluteUri.ToString(), EnvironmentVariableTarget.Process);
            Console.WriteLine(proxyUri.Host.ToString());
        }

        private void initial_read_mongo()
        {
            var client = new MongoClient(@"mongodb://yxiao:ec601@ec601-app-cluster-shard-00-00-dishd.mongodb.net:27017,ec601-app-cluster-shard-00-01-dishd.mongodb.net:27017,ec601-app-cluster-shard-00-02-dishd.mongodb.net:27017/test?ssl=true&replicaSet=ec601-app-cluster-shard-0&authSource=admin&retryWrites=true");
            var database = client.GetDatabase("ec601-app-cluster");
            debug.Text = "mongodb connected";

            var collection = database.GetCollection<BsonDocument>("api_data");

            var filter = Builders<BsonDocument>.Filter.Empty;
            var result = collection.Find(filter).ToList();
            foreach (var doc in result)
            {
                Console.WriteLine(doc.ToJson());
                try
                {
                    string tmp_url = doc["image_url"].ToString();
                    mongo_lb.Items.Add(tmp_url);
                    debug.Text = "";
                }
                catch
                {
                    debug.Text = "bad data point";
                }
            }
        }

        private void update_mongo_dataview()
        {
            var client = new MongoClient(@"mongodb://yxiao:ec601@ec601-app-cluster-shard-00-00-dishd.mongodb.net:27017,ec601-app-cluster-shard-00-01-dishd.mongodb.net:27017,ec601-app-cluster-shard-00-02-dishd.mongodb.net:27017/test?ssl=true&replicaSet=ec601-app-cluster-shard-0&authSource=admin&retryWrites=true");
            var database = client.GetDatabase("ec601-app-cluster");
            debug.Text = "mongodb connected";

            var collection = database.GetCollection<BsonDocument>("api_data");

            var filter = Builders<BsonDocument>.Filter.Empty;
            var result = collection.Find(filter).ToList();

            DataTable table = new DataTable();
            table.Columns.Add(new DataColumn("Id", typeof(string)));
            table.Columns.Add(new DataColumn("image_url", typeof(string)));
            table.Columns.Add(new DataColumn("time", typeof(string)));
            table.Columns.Add(new DataColumn("descriptor", typeof(string)));
            DataRow row;
            foreach (var doc in result)
            {
                Console.WriteLine(doc.ToJson());
  
                string tmp_url = doc["image_url"].ToString();
                string Id = doc["Id"].ToString();
                string time = doc["time"].ToString();
                string desp = doc["descripitor"].ToString();
                row = table.NewRow();
                row["id"] = Id;
                row["image_url"] = tmp_url;
                row["time"] = time;
                row["descriptor"] = desp;
                table.Rows.Add(row);

            }
            mongo_dgv.DataSource = table;
        }

        private void update_stats_dataview()
        {
            var client = new MongoClient(@"mongodb://yxiao:ec601@ec601-app-cluster-shard-00-00-dishd.mongodb.net:27017,ec601-app-cluster-shard-00-01-dishd.mongodb.net:27017,ec601-app-cluster-shard-00-02-dishd.mongodb.net:27017/test?ssl=true&replicaSet=ec601-app-cluster-shard-0&authSource=admin&retryWrites=true");
            var database = client.GetDatabase("ec601-app-cluster");
            debug.Text = "mongodb connected";

            var collection = database.GetCollection<BsonDocument>("api_data");

            var filter = Builders<BsonDocument>.Filter.Empty;
            var result = collection.Find(filter).ToList();

            DataTable table = new DataTable();
            table.Columns.Add(new DataColumn("Name", typeof(string)));
            table.Columns.Add(new DataColumn("Value", typeof(string)));

            int count = 0;
            Hashtable desp_table = new Hashtable();
            foreach (var doc in result)
            {
                count = count + 1;
                string desp = doc["descripitor"].ToString();
                if (desp_table.ContainsKey(desp))
                {
                    desp_table[desp] = (Convert.ToInt32(desp_table[desp]) + 1);
                }
                else
                {
                    desp_table[desp] = 0;
                }
            }
            DataRow num_row = table.NewRow();
            num_row["Name"] = "tweet number";
            num_row["Value"] = count.ToString();
            table.Rows.Add(num_row);

            KeyValuePair<string, int> max = new KeyValuePair<string, int>();
            int max_val = 0;
            int val;
            string max_desp = "N/A";
            foreach (var key in desp_table.Keys)
            {
                val = Convert.ToInt32(desp_table[key]);
                if (val > max_val)
                {
                    max_val = val;
                    max_desp = key.ToString();
                }
            }
            DataRow desp_row = table.NewRow();
            desp_row["Name"] = "popular desp";
            desp_row["Value"] = max_desp;
            table.Rows.Add(desp_row);

            stats_dataview.DataSource = table;
        }

        private void stream_bt_Click(object sender, EventArgs e)
        {
            // get a new twitter image url from handle
            string img_url = stream.next();
            twitter_pb.Load(img_url);
            //annotate_image(img_url);

            // insert image url to database
            string connect_str = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\API_App_db.mdf;Integrated Security=True"; // connnection string
            string curr_time = DateTime.Now.ToString();
            string curr_desp = accont_tb.Text;
            if (!mongo_cb.Checked)
            {
                debug.Text = "using localdb";
                String query = @"insert into tweets (Id, image_url, time, descriptor) values ('" + this.tweet_count.ToString() + "','" + img_url + "','" + curr_time + "','" + curr_desp + "')";               // insert SQL command
                SqlConnection dbconnect = new SqlConnection(connect_str);
                SqlCommand dbcomm = new SqlCommand(query);
            
                try
                {
                    dbconnect.Open();
                    dbcomm.Connection = dbconnect;// 
                    dbcomm.ExecuteNonQuery();     // execute an insert command to database
                    this.tweetsTableAdapter.Fill(this.aPI_App_dbDataSet.tweets);  // refresh listbox
                    tweet_list.SelectedIndex = this.tweet_count;                  // select the latest url in the list box
                    this.tweet_count = this.tweet_count + 1;                      // increase count by 1  
                }
                catch
                {
                    debug.Text = "fail to insert new data";
                }
            } else
            {
                debug.Text = "using mongodb";
                var client = new MongoClient(@"mongodb://yxiao:ec601@ec601-app-cluster-shard-00-00-dishd.mongodb.net:27017,ec601-app-cluster-shard-00-01-dishd.mongodb.net:27017,ec601-app-cluster-shard-00-02-dishd.mongodb.net:27017/test?ssl=true&replicaSet=ec601-app-cluster-shard-0&authSource=admin&retryWrites=true");
                var database = client.GetDatabase("ec601-app-cluster");
                var collection = database.GetCollection<BsonDocument>("api_data");
                int cur_id = mongo_lb.Items.Count;
                var document = new BsonDocument{
                    { "Id", (cur_id+1).ToString() },
                    { "image_url", img_url},
                    { "time", curr_time},
                    { "descripitor", curr_desp}
                };
                collection.InsertOne(document);
                var filter = Builders<BsonDocument>.Filter.Empty;
                var result = collection.Find(filter).ToList();
                mongo_lb.Items.Clear();
                foreach (var doc in result)
                {
                    Console.WriteLine(doc.ToJson());
                    try
                    {
                        string tmp_url = doc["image_url"].ToString();
                        mongo_lb.Items.Add(tmp_url);
                        debug.Text = "";
                    }
                    catch
                    {
                        debug.Text = "bad data point";
                    }
                }
                update_mongo_dataview();
                update_stats_dataview();
            }

        }

        private void update_mongo_listbox()
        {
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: 这行代码将数据加载到表“aPI_App_dbDataSet.tweets”中。您可以根据需要移动或删除它。
            this.tweetsTableAdapter.Fill(this.aPI_App_dbDataSet.tweets);

        }

        private void tweet_list_Click(object sender, EventArgs e)
        {
            try
            {
                DataRowView cur_row = (DataRowView)tweet_list.SelectedItem;
                string url = (string)cur_row.Row["image_url"];    // get image url from listbox row
                //annotate_image(url);
                twitter_pb.Load(url);   // load image based on new url
            }
            catch
            {
                ;
            }
        }

        private void annotate_image(string url)
        {
            Google.Cloud.Vision.V1.Image image = Google.Cloud.Vision.V1.Image.FromUri(url);
            ImageAnnotatorClient client = ImageAnnotatorClient.Create();
            var response = client.DetectFaces(image);
            foreach (var annotation in response)
            {
                Console.WriteLine($"Picture: {url}");
                Console.WriteLine($" Surprise: {annotation.SurpriseLikelihood}");
            }
            /*
            IReadOnlyList<EntityAnnotation> labels = client.DetectLabels(image3);
            foreach (EntityAnnotation label in labels)
            {
                debug.Text = $"Score: {(int)(label.Score * 100)}%; Description: {label.Description}";
            }
            */
        }

        private void change_acc_bt_Click(object sender, EventArgs e)
        {
            // Instantiate a new streamer
            string twitter_account = accont_tb.Text;
            var streamer = stream_module.stream(twitter_account);
            stream = streamer.streamImage();
            debug.Text = "change to: " + twitter_account;
        }

        private void clear_bt_Click(object sender, EventArgs e)
        {
            // connect to database
            string connect_str = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\API_App_db.mdf;Integrated Security=True"; // connnection string
            SqlConnection dbconnect = new SqlConnection(connect_str);
            SqlCommand dbcomm;
            dbconnect.Open();

            string cur_id;
            // clear the database
            foreach (DataRowView drv in tweet_source.List)
            {
                cur_id = drv.Row["Id"].ToString();
                string query = @"delete from tweets where Id = " + cur_id;
                dbcomm = new SqlCommand(query);
                dbcomm.Connection = dbconnect;// 
                dbcomm.ExecuteNonQuery();     // execute an delete command to database
                this.tweetsTableAdapter.Fill(this.aPI_App_dbDataSet.tweets);  // refresh listbox
            }

            twitter_pb.Load("https://vignette.wikia.nocookie.net/nichijou/images/1/12/Sakamoto_in_box_ep3.png/revision/latest?cb=20110829063401");
        }

        private void mongo_lb_Click(object sender, EventArgs e)
        {
            try
            {
                string url = mongo_lb.SelectedItem.ToString();    // get image url from listbox row
                twitter_pb.Load(url);   // load image based on new url
            }
            catch
            {
                ;
            }
        }
    }
}
