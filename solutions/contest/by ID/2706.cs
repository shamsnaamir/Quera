using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace problem19
{
    class Program
    {
        static void print(string a)
        {
            Console.WriteLine(a);
        }
        static int max(int b, int a)
        {
            if (a > b)
                return a;
            return b;
        }
        static string input()
        {
            return Console.ReadLine();
        }
        static int N = 2000;
        static List<bool> seen = new List<bool>();
        static List<int> a = new List<int>();
        static void Main(string[] args)
        {


            string[] x = (input()).Split(' ');
            int a, b, c;
            b = int.Parse(x[0]);
            a = int.Parse(x[1]);
            while (true)
            {
                while (a != 0 && b != 0)
                {
                    a -= 1;
                    b -= 1;
                    b += 1;
                }
                if (a + b == 1)
                    break;
                if (a == 0)
                    while (b > 1)
                    {
                        b -= 2;
                        a += 1;
                    }
                if (a + b == 1)
                    break;
                if (b == 0)
                {
                    while (a > 1)
                        a -= 2;
                    a += 1;
                }
                if (a + b == 1)
                    break;
            }
            if (a == 1)
                print("white");
            else
                print("black");

            Console.ReadKey();
        }
    }
}