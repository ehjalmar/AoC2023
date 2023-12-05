using Day5;

var lines = File.ReadAllLines("input.txt");

ProcessPart1(lines);

Console.WriteLine("Press ENTER to exit!");
Console.ReadLine();

static void ProcessPart1(string[] lines)
{
    var seeds = lines.First().Split(':')[1].Split(" ", StringSplitOptions.RemoveEmptyEntries);
    var mappings = new List<Mapping>();
    var currentSourceType = "";
    var currentDestinationType = "";
    var seedLocationMapping = new Dictionary<Int64, Int64>();

    for (int i = 1; i < lines.Length; i++) {

        if (lines[i] == "") continue;
        // We´re at a heading
        else if (lines[i].Contains(':')) // seed-to-soil map:
        {
            var mappingType = lines[i].Split(' ')[0].Split('-');
            currentDestinationType = mappingType.Last();
            currentSourceType = mappingType.First();
            //Console.WriteLine("Destination: " + currentDestinationType);
            //Console.WriteLine("Source " + currentSourceType);
        }
        else // 50 98 2
        {
            var rowMappings = lines[i].Split(" ");
            var rangeLength = Int64.Parse(rowMappings[2]);
            var startSoruce = Int64.Parse(rowMappings[1]);
            var startDestination = Int64.Parse(rowMappings[0]);

            var newMapping = new Mapping()
            {
                Destination = currentDestinationType,
                Source = currentSourceType,
                DestinationIndex = startDestination,
                SourceIndex = startSoruce,
                Skew = startDestination-startSoruce,
                Range = rangeLength
            };
            mappings.Add(newMapping);
        }
    }

    foreach(var currentSeed in seeds)
    {
        //Console.WriteLine("Seed: " + currentSeed + " Soil: " + LookupDestination(mappings, "seed", "soil", int.Parse(currentSeed)));
        var soilIndex = LookupDestination(mappings, "seed", "soil", Int64.Parse(currentSeed));
        var fertilizerIndex = LookupDestination(mappings, "soil", "fertilizer", soilIndex);
        var waterIndex = LookupDestination(mappings, "fertilizer", "water", fertilizerIndex);
        var lightIndex = LookupDestination(mappings, "water", "light", waterIndex);
        var temperatureIndex = LookupDestination(mappings, "light", "temperature", lightIndex);
        var humidityIndex = LookupDestination(mappings, "temperature", "humidity", temperatureIndex);
        var locationIndex = LookupDestination(mappings, "humidity", "location", humidityIndex);
        seedLocationMapping.Add(Int64.Parse(currentSeed), locationIndex);
    }

    Console.WriteLine(seedLocationMapping.OrderBy(x => x.Value).First().Value);

}

static Int64 LookupDestination(List<Mapping> mappings, string sourceType, string destinationType, Int64 sourceIndex)
{
    var mappingsForType = mappings.Where(x =>
    x.Destination == destinationType
    && x.Source == sourceType);

    foreach (var item in mappingsForType)
    {
        if(item.SourceIndex <= sourceIndex && sourceIndex <= item.SourceIndex + item.Range) // 52 50 48
        {
            // Found mapping!
            return sourceIndex + item.Skew;
        }
    }

    // DIdn´t find any mapping...
    return sourceIndex;
}
