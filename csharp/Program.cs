using System;
using System.Windows.Forms;

namespace csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            SendKeys.SendWait("Wowsers!");
        }
    }
}
