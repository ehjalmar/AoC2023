using Day5_2;

var lines = File.ReadAllLines("input.txt");

ProcessPart2(lines);

Console.WriteLine("Press ENTER to exit!");
Console.ReadLine();


static void ProcessPart2(string[] lines)
{
    var watch = System.Diagnostics.Stopwatch.StartNew();

    var seedsRanges = lines.First().Split(':')[1].Split(" ", StringSplitOptions.RemoveEmptyEntries);
    var seeds = new Dictionary<Int64, Int64>();
    for (int i = 0; i < seedsRanges.Length; i += 2)
    {
        var start = Int64.Parse(seedsRanges[i]);
        var countOfSeeds = Int64.Parse(seedsRanges[i + 1]);
        seeds.Add(start, countOfSeeds);
    }

    var mappings = new List<Mapping>();
    var currentSourceType = "";
    var currentDestinationType = "";
    var seedLocationMapping = new Dictionary<Int64, Int64>();

    for (int i = 1; i < lines.Length; i++)
    {

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
                Skew = startDestination - startSoruce,
                Range = rangeLength
            };
            mappings.Add(newMapping);
        }
    }

    var locationMappings = mappings.Where(x => x.Destination == "location")
        .OrderBy(x => x.DestinationIndex);

    Int64 lowestSeed = 9999999999999;
    Int64 lowestSeedLocation = 9999999999999;

    // Start with smallest location mapping we have and calculate backwards until we find one with a matching seed
    foreach (var locationMapping in locationMappings)
    {
        for (int i = 0; i < locationMapping.Range; i++)
        { 
            var humidityIndex = LookupSource(mappings, "humidity", "location", locationMapping.DestinationIndex+i);
            var temperatureIndex = LookupSource(mappings, "temperature", "humidity", humidityIndex);
            var lightIndex = LookupSource(mappings, "light", "temperature", temperatureIndex);
            var waterIndex = LookupSource(mappings, "water", "light", lightIndex);
            var fertilizerIndex = LookupSource(mappings, "fertilizer", "water", waterIndex);
            var soilIndex = LookupSource(mappings, "soil", "fertilizer", fertilizerIndex);
            var seedIndex = LookupSource(mappings, "seed", "soil", soilIndex);

            //Parallel.ForEach(seeds, currentSeedMapping =>
            foreach (var currentSeedMapping in seeds)
            {
                if (seedIndex < lowestSeed
                && currentSeedMapping.Key <= seedIndex
                && seedIndex <= currentSeedMapping.Key + currentSeedMapping.Value) // Found seed in one of the original ranges
                {
                    lowestSeed = currentSeedMapping.Key;
                    lowestSeedLocation = locationMapping.DestinationIndex;
                    break;
                }
            }
            if (lowestSeed < 9999999999999)
                break;
        }
        if (lowestSeed < 9999999999999)
            break;
    }
    Console.WriteLine("Seed : " + lowestSeed + " Location: " + lowestSeedLocation);

    watch.Stop();
    var elapsedMs = watch.ElapsedMilliseconds;
    Console.WriteLine("elapsedMs : " + elapsedMs);
}

static Int64 LookupDestination(List<Mapping> mappings, string sourceType, string destinationType, Int64 sourceIndex)
{
    var mappingsForType = mappings.Where(x =>
    x.Destination == destinationType
    && x.Source == sourceType);

    foreach (var item in mappingsForType.OrderBy(x => x.SourceIndex))
    {
        if (item.SourceIndex <= sourceIndex && sourceIndex <= item.SourceIndex + item.Range) // 52 50 48
        {
            // Found mapping!
            return sourceIndex + item.Skew;
        }
    }

    // DIdn´t find any mapping...
    return sourceIndex;
}

static Int64 LookupSource(List<Mapping> mappings, string sourceType, string destinationType, Int64 destinationIndex)
{
    var mappingsForType = mappings.Where(x =>
    x.Destination == destinationType
    && x.Source == sourceType);

    foreach (var item in mappingsForType)
    {
        if (item.DestinationIndex <= destinationIndex && destinationIndex <= item.DestinationIndex + item.Range) // 52 50 48
        {
            // Found mapping!
            return destinationIndex - item.Skew;
        }
    }

    // DIdn´t find any mapping...
    return destinationIndex;
}
