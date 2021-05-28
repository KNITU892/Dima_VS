using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
namespace T_34
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private void Form1_Load(object sender, EventArgs e)
		{

		}

		private void pictureBox1_Click(object sender, EventArgs e)
		{
			Graphics g = pictureBox1.CreateGraphics();
			g.Clear(Color.GreenYellow);
			SolidBrush myCorp = new SolidBrush(Color.DarkGreen);
			SolidBrush myTrum = new SolidBrush(Color.DarkGreen);
			SolidBrush myVoluina = new SolidBrush(Color.DarkGreen);
			SolidBrush myHead = new SolidBrush(Color.Black);
			Pen myWind = new Pen(Color.Black, 2);
			g.FillPolygon(myCorp, new Point[]
			  {
	new Point(100,300),new Point(700,300),
	new Point(700,300),new Point(600,400),
	new Point(600,400),new Point(200,400),
	new Point(200,400),new Point(100,300)
			  }
			);
			g.FillRectangle(myTrum, 250, 200, 350, 100);
			g.FillRectangle(myVoluina, 150, 220, 200, 30);
			g.FillRectangle(myHead, 370, 190, 80, 20);
			for (int y = 200; y <= 600; y += 70)
			{
				g.DrawEllipse(myWind, y, 370, 40, 40); // 6 окружностей
			}
		}
	}
}
