namespace API_App
{
    partial class Form1
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.debug = new System.Windows.Forms.Label();
            this.twitter_pb = new System.Windows.Forms.PictureBox();
            this.stream_bt = new System.Windows.Forms.Button();
            this.tweet_list = new System.Windows.Forms.ListBox();
            this.tweet_source = new System.Windows.Forms.BindingSource(this.components);
            this.aPI_App_dbDataSet = new API_App.API_App_dbDataSet();
            this.tweetsTableAdapter = new API_App.API_App_dbDataSetTableAdapters.tweetsTableAdapter();
            this.accont_tb = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.change_acc_bt = new System.Windows.Forms.Button();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.idDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.imageurlDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.time = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.descriptor = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.clear_bt = new System.Windows.Forms.Button();
            this.mongo_lb = new System.Windows.Forms.ListBox();
            this.mongo_cb = new System.Windows.Forms.CheckBox();
            this.cloud_panel = new System.Windows.Forms.Panel();
            this.cl_del_bt = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.mongo_dgv = new System.Windows.Forms.DataGridView();
            this.stats_dataview = new System.Windows.Forms.DataGridView();
            ((System.ComponentModel.ISupportInitialize)(this.twitter_pb)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tweet_source)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.aPI_App_dbDataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.cloud_panel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.mongo_dgv)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.stats_dataview)).BeginInit();
            this.SuspendLayout();
            // 
            // debug
            // 
            this.debug.AutoSize = true;
            this.debug.Location = new System.Drawing.Point(383, 326);
            this.debug.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.debug.Name = "debug";
            this.debug.Size = new System.Drawing.Size(35, 12);
            this.debug.TabIndex = 0;
            this.debug.Text = "debug";
            // 
            // twitter_pb
            // 
            this.twitter_pb.Image = ((System.Drawing.Image)(resources.GetObject("twitter_pb.Image")));
            this.twitter_pb.Location = new System.Drawing.Point(9, 25);
            this.twitter_pb.Margin = new System.Windows.Forms.Padding(2);
            this.twitter_pb.Name = "twitter_pb";
            this.twitter_pb.Size = new System.Drawing.Size(370, 313);
            this.twitter_pb.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.twitter_pb.TabIndex = 1;
            this.twitter_pb.TabStop = false;
            // 
            // stream_bt
            // 
            this.stream_bt.Location = new System.Drawing.Point(14, 36);
            this.stream_bt.Margin = new System.Windows.Forms.Padding(2);
            this.stream_bt.Name = "stream_bt";
            this.stream_bt.Size = new System.Drawing.Size(75, 25);
            this.stream_bt.TabIndex = 2;
            this.stream_bt.Text = "Fetch";
            this.stream_bt.UseVisualStyleBackColor = true;
            this.stream_bt.Click += new System.EventHandler(this.stream_bt_Click);
            // 
            // tweet_list
            // 
            this.tweet_list.DataSource = this.tweet_source;
            this.tweet_list.DisplayMember = "image_url";
            this.tweet_list.FormattingEnabled = true;
            this.tweet_list.ItemHeight = 12;
            this.tweet_list.Location = new System.Drawing.Point(385, 59);
            this.tweet_list.Margin = new System.Windows.Forms.Padding(2);
            this.tweet_list.Name = "tweet_list";
            this.tweet_list.Size = new System.Drawing.Size(207, 256);
            this.tweet_list.TabIndex = 3;
            this.tweet_list.ValueMember = "Id";
            this.tweet_list.Click += new System.EventHandler(this.tweet_list_Click);
            // 
            // tweet_source
            // 
            this.tweet_source.DataMember = "tweets";
            this.tweet_source.DataSource = this.aPI_App_dbDataSet;
            // 
            // aPI_App_dbDataSet
            // 
            this.aPI_App_dbDataSet.DataSetName = "API_App_dbDataSet";
            this.aPI_App_dbDataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // tweetsTableAdapter
            // 
            this.tweetsTableAdapter.ClearBeforeFill = true;
            // 
            // accont_tb
            // 
            this.accont_tb.Location = new System.Drawing.Point(798, 25);
            this.accont_tb.Margin = new System.Windows.Forms.Padding(2);
            this.accont_tb.Name = "accont_tb";
            this.accont_tb.Size = new System.Drawing.Size(210, 21);
            this.accont_tb.TabIndex = 4;
            this.accont_tb.Text = "@keinishikori";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(796, 9);
            this.label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(155, 12);
            this.label1.TabIndex = 5;
            this.label1.Text = "provide a twitter account";
            // 
            // change_acc_bt
            // 
            this.change_acc_bt.Location = new System.Drawing.Point(14, 65);
            this.change_acc_bt.Margin = new System.Windows.Forms.Padding(2);
            this.change_acc_bt.Name = "change_acc_bt";
            this.change_acc_bt.Size = new System.Drawing.Size(75, 25);
            this.change_acc_bt.TabIndex = 6;
            this.change_acc_bt.Text = "Change";
            this.change_acc_bt.UseVisualStyleBackColor = true;
            this.change_acc_bt.Click += new System.EventHandler(this.change_acc_bt_Click);
            // 
            // dataGridView1
            // 
            this.dataGridView1.AutoGenerateColumns = false;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.idDataGridViewTextBoxColumn,
            this.imageurlDataGridViewTextBoxColumn,
            this.time,
            this.descriptor});
            this.dataGridView1.DataSource = this.tweet_source;
            this.dataGridView1.Location = new System.Drawing.Point(9, 343);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.ReadOnly = true;
            this.dataGridView1.RowTemplate.Height = 23;
            this.dataGridView1.Size = new System.Drawing.Size(370, 216);
            this.dataGridView1.TabIndex = 9;
            // 
            // idDataGridViewTextBoxColumn
            // 
            this.idDataGridViewTextBoxColumn.DataPropertyName = "Id";
            this.idDataGridViewTextBoxColumn.HeaderText = "Id";
            this.idDataGridViewTextBoxColumn.Name = "idDataGridViewTextBoxColumn";
            this.idDataGridViewTextBoxColumn.ReadOnly = true;
            this.idDataGridViewTextBoxColumn.Width = 50;
            // 
            // imageurlDataGridViewTextBoxColumn
            // 
            this.imageurlDataGridViewTextBoxColumn.DataPropertyName = "image_url";
            this.imageurlDataGridViewTextBoxColumn.HeaderText = "image_url";
            this.imageurlDataGridViewTextBoxColumn.Name = "imageurlDataGridViewTextBoxColumn";
            this.imageurlDataGridViewTextBoxColumn.ReadOnly = true;
            // 
            // time
            // 
            this.time.DataPropertyName = "time";
            this.time.HeaderText = "time";
            this.time.Name = "time";
            this.time.ReadOnly = true;
            // 
            // descriptor
            // 
            this.descriptor.DataPropertyName = "descriptor";
            this.descriptor.HeaderText = "descriptor";
            this.descriptor.Name = "descriptor";
            this.descriptor.ReadOnly = true;
            // 
            // clear_bt
            // 
            this.clear_bt.Location = new System.Drawing.Point(14, 95);
            this.clear_bt.Name = "clear_bt";
            this.clear_bt.Size = new System.Drawing.Size(75, 25);
            this.clear_bt.TabIndex = 10;
            this.clear_bt.Text = "Clear";
            this.clear_bt.UseVisualStyleBackColor = true;
            this.clear_bt.Click += new System.EventHandler(this.clear_bt_Click);
            // 
            // mongo_lb
            // 
            this.mongo_lb.Cursor = System.Windows.Forms.Cursors.Default;
            this.mongo_lb.FormattingEnabled = true;
            this.mongo_lb.ItemHeight = 12;
            this.mongo_lb.Location = new System.Drawing.Point(597, 59);
            this.mongo_lb.Name = "mongo_lb";
            this.mongo_lb.Size = new System.Drawing.Size(195, 256);
            this.mongo_lb.TabIndex = 11;
            this.mongo_lb.Click += new System.EventHandler(this.mongo_lb_Click);
            // 
            // mongo_cb
            // 
            this.mongo_cb.AutoSize = true;
            this.mongo_cb.Location = new System.Drawing.Point(14, 15);
            this.mongo_cb.Name = "mongo_cb";
            this.mongo_cb.Size = new System.Drawing.Size(108, 16);
            this.mongo_cb.TabIndex = 12;
            this.mongo_cb.Text = "cloud database";
            this.mongo_cb.UseVisualStyleBackColor = true;
            // 
            // cloud_panel
            // 
            this.cloud_panel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.cloud_panel.Controls.Add(this.cl_del_bt);
            this.cloud_panel.Controls.Add(this.mongo_cb);
            this.cloud_panel.Controls.Add(this.clear_bt);
            this.cloud_panel.Controls.Add(this.stream_bt);
            this.cloud_panel.Controls.Add(this.change_acc_bt);
            this.cloud_panel.Location = new System.Drawing.Point(798, 59);
            this.cloud_panel.Name = "cloud_panel";
            this.cloud_panel.Size = new System.Drawing.Size(210, 256);
            this.cloud_panel.TabIndex = 13;
            // 
            // cl_del_bt
            // 
            this.cl_del_bt.Location = new System.Drawing.Point(14, 126);
            this.cl_del_bt.Name = "cl_del_bt";
            this.cl_del_bt.Size = new System.Drawing.Size(75, 23);
            this.cl_del_bt.TabIndex = 13;
            this.cl_del_bt.Text = "Delete";
            this.cl_del_bt.UseVisualStyleBackColor = true;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(385, 25);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 14;
            this.label2.Text = "Local Data";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(595, 25);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(65, 12);
            this.label3.TabIndex = 15;
            this.label3.Text = "Cloud Data";
            // 
            // mongo_dgv
            // 
            this.mongo_dgv.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.mongo_dgv.Location = new System.Drawing.Point(387, 343);
            this.mongo_dgv.Name = "mongo_dgv";
            this.mongo_dgv.ReadOnly = true;
            this.mongo_dgv.RowTemplate.Height = 23;
            this.mongo_dgv.Size = new System.Drawing.Size(348, 216);
            this.mongo_dgv.TabIndex = 16;
            // 
            // stats_dataview
            // 
            this.stats_dataview.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.stats_dataview.Location = new System.Drawing.Point(741, 343);
            this.stats_dataview.Name = "stats_dataview";
            this.stats_dataview.RowTemplate.Height = 23;
            this.stats_dataview.Size = new System.Drawing.Size(267, 216);
            this.stats_dataview.TabIndex = 17;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1021, 571);
            this.Controls.Add(this.stats_dataview);
            this.Controls.Add(this.mongo_dgv);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.cloud_panel);
            this.Controls.Add(this.mongo_lb);
            this.Controls.Add(this.dataGridView1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.accont_tb);
            this.Controls.Add(this.tweet_list);
            this.Controls.Add(this.twitter_pb);
            this.Controls.Add(this.debug);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(1037, 610);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(1037, 590);
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "API App";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.twitter_pb)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tweet_source)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.aPI_App_dbDataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.cloud_panel.ResumeLayout(false);
            this.cloud_panel.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.mongo_dgv)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.stats_dataview)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label debug;
        private System.Windows.Forms.PictureBox twitter_pb;
        private System.Windows.Forms.Button stream_bt;
        private System.Windows.Forms.ListBox tweet_list;
        private System.Windows.Forms.BindingSource tweet_source;
        private API_App_dbDataSet aPI_App_dbDataSet;
        private API_App_dbDataSetTableAdapters.tweetsTableAdapter tweetsTableAdapter;
        private System.Windows.Forms.TextBox accont_tb;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button change_acc_bt;
        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.DataGridViewTextBoxColumn idDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn imageurlDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn time;
        private System.Windows.Forms.DataGridViewTextBoxColumn descriptor;
        private System.Windows.Forms.Button clear_bt;
        private System.Windows.Forms.ListBox mongo_lb;
        private System.Windows.Forms.CheckBox mongo_cb;
        private System.Windows.Forms.Panel cloud_panel;
        private System.Windows.Forms.Button cl_del_bt;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.DataGridView mongo_dgv;
        private System.Windows.Forms.DataGridView stats_dataview;
    }
}

