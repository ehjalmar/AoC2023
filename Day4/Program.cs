// See https://aka.ms/new-console-template for more information

using System.Runtime.InteropServices;
using System.Threading.Tasks.Sources;

var lines = File.ReadAllLines("input.txt");

ProcessPart1(lines);
ProcessPart2(lines);

Console.ReadLine();

static void ProcessPart1(string[] lines)
{
    var totalScores = 0;

    for (int i = 0; i < lines.Length; i++)
    {
        // Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        var currentItem = lines[i];
        //Console.WriteLine(currentItem);
        var pipeSplit = currentItem.Split("|");
        var winningNumbers = pipeSplit[0].Split(":")[1].Split(" ", StringSplitOptions.RemoveEmptyEntries);
        var numbersOnHand = pipeSplit[1].Split(" ", StringSplitOptions.RemoveEmptyEntries).ToList();

        // Check how many of winning numbers exists in hand
        var existingWinningNumbers = winningNumbers.Where(x => numbersOnHand.Contains(x));

        var score = 0;

        if (existingWinningNumbers.Any())
        {
            for (int foo = 0; foo < existingWinningNumbers.Count(); foo++)
            {
                if (foo == 0)
                {
                    score = 1;
                    continue;
                }
                score *= 2;
            }
        }
        //Console.WriteLine(score);
        totalScores += score;
    }
    Console.WriteLine(totalScores);
}


static void ProcessPart2(string[] lines)
{
    var winningNumbersPerRow = new Dictionary<int,int>();
    var extraRowsPerIndex = new Dictionary<int, int>();

    for (int i = 1; i <= lines.Length; i++)
    {
        // Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        var currentItem = lines[i-1];
        //Console.WriteLine(currentItem);
        var pipeSplit = currentItem.Split("|");
        var winningNumbers = pipeSplit[0].Split(":")[1].Split(" ", StringSplitOptions.RemoveEmptyEntries);
        var numbersOnHand = pipeSplit[1].Split(" ", StringSplitOptions.RemoveEmptyEntries).ToList();

        // Check how many of winning numbers exists in hand
        var existingWinningNumbers = winningNumbers.Where(x => numbersOnHand.Contains(x));
        winningNumbersPerRow.Add(i, existingWinningNumbers.Count());

        var currentWinningNumbers = existingWinningNumbers.Count();
        var foo = extraRowsPerIndex.ContainsKey(i) ? extraRowsPerIndex[i] + 1 : 1;
        for (int y = 0; y < foo; y++)
        {
            for (int j = 1; j <= currentWinningNumbers; j++)
            {
                if (!extraRowsPerIndex.ContainsKey(i + j))
                {
                    extraRowsPerIndex[i + j] = 1;
                }
                else
                {
                    extraRowsPerIndex[i + j] += 1;

                }
            }
        }
    }

    // for each row, add additional rows
    var numberOfCards = 0;
    for (int i = 1; i <= lines.Length; i++)
    {
        if (!extraRowsPerIndex.ContainsKey(i))
        {
            //Console.WriteLine("Card " + i + " 1");
            numberOfCards++;
        }
        else
        {
            //Console.WriteLine("Card " + i + " " + (1 + extraRowsPerIndex[i]));
            numberOfCards += 1 + extraRowsPerIndex[i];
        }
    }
        
        Console.WriteLine("Number of cards: " + numberOfCards + "!");
}