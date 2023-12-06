using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day5_2
{
    internal class Mapping
    {
        public string Source { get; set; }
        public string Destination { get; set; }
        public Int64 SourceIndex { get; set; }
        public Int64 DestinationIndex { get; set; }
        public Int64 Skew { get; set; }
        public Int64 Range { get; set; }
    }
}
