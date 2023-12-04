// See https://aka.ms/new-console-template for more information

using System.Threading.Tasks.Sources;

var lines = File.ReadAllLines("input.txt");
var totalScores = 0;

for (int i = 0; i < lines.Length; i++)
{
    // Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    var currentItem = lines[i];
    Console.WriteLine(currentItem);
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
    Console.WriteLine(score);
    totalScores += score;
}
Console.WriteLine(totalScores);
Console.ReadLine();