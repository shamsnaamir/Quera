using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace problem19
{
    class Program
    {
        static void Main(string[] args)
        {

            string[] a = Console.ReadLine().Split(' ');
            string[] b = Console.ReadLine().Split(' ');
            int x1 = int.Parse(a[0]);
            int x2 = int.Parse(b[0]);
            if (x1 > x2)
            {
                Console.Write("Left");
            }
            else
            {
                Console.Write("Right");
            }
        }
    }
}

