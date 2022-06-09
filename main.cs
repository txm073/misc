using System;
 
namespace SimpleMaths
{
    public class Operations
    {
        [DllExport]
        public static int add(int a, int b)
        {
            return a + b;
        }
 
        public static int substract(int a, int b)
        {
            return a - b;
        }
 
        public static int multiply(int a, int b)
        {
            return a * b;
        }
    }
}
