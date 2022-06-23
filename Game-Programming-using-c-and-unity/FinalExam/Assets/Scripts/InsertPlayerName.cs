using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;

public class InsertPlayerName : MonoBehaviour {
    public static string ConstantName;

    public static string score1, score2;

    public InputField PlayerName;
    public static string playerScore1, playerScore2, playerScore3;
    public Text currentPlayerData;

    private static int defaultScore = 0;
    public string[] ReadPlayerData;
    private static string data;
    private static string defaultPath = "Assets/PlayerData/";
    //public void Text_Changed(string newText)
    //{
    //    float temp = float.Parse(newText);
    //}

   
   
    public void LoadPlayerData()
    {
        ConstantName = PlayerName.text.ToString();
        if (File.Exists(defaultPath + PlayerName.text.ToString() + ".txt"))

        {
            StreamReader reader = new StreamReader(defaultPath + PlayerName.text.ToString() + ".txt");
            ReadPlayerData = new string[File.ReadAllLines(defaultPath + PlayerName.text.ToString() + ".txt").Length];
            string line;
            int i = 0;
            while ((line = reader.ReadLine()) != null)
            {
                ReadPlayerData[i] = line;
                i++;
            }
            reader.Close();
            currentPlayerData.text = ReadPlayerData[1].ToString() + "\n" + ReadPlayerData[2].ToString() + "\n" + ReadPlayerData[3].ToString();
            score1 = ReadPlayerData[1];
            score2 = ReadPlayerData[2];
        }
        else
            AddPlayerName();
    }

    public void AddPlayerName()
    {
        StreamWriter writer = new StreamWriter(defaultPath + ConstantName + ".txt");
        writer.WriteLine(PlayerName.text.ToString());
        for (int e = 0; e < 3; e++)
        {
            writer.WriteLine(defaultScore.ToString());
        }
        writer.Close();

        StreamReader reader = new StreamReader(defaultPath + PlayerName.text.ToString() + ".txt");
        ReadPlayerData = new string[File.ReadAllLines(defaultPath + PlayerName.text.ToString() + ".txt").Length];
        string line;
        int i = 0;
        while ((line = reader.ReadLine()) != null)
        {
            ReadPlayerData[i] = line;
            i++;
        }
        reader.Close();
        currentPlayerData.text = ReadPlayerData[1].ToString() + "\n" + ReadPlayerData[2].ToString() + "\n" + ReadPlayerData[3].ToString();
        score1 = ReadPlayerData[1];
        score2 = ReadPlayerData[2];
    }
}
