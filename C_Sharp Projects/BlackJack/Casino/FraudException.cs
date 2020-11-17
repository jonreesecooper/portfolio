using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Casino
{
    public class FraudException: Exception
    {
        public FraudException()
            : base() { }
        // this is inheriting from base(), which is Exception (what the class inherits from)
        public FraudException(string message)
            : base(message) { }
        // overloaded constructor that takes in a message parameter
    }
}
