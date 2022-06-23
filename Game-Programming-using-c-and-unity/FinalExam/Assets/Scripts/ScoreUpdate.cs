using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class ScoreUpdate : MonoBehaviour {

    public static int newScore;
    public Text NewScore;

    private void Start()
    {
        newScore = 0;
    }
    public void IncreaseScore()
    {
        newScore += 1;
        NewScore.text = newScore.ToString();
        Debug.Log(newScore);
    }

    public void DecreaseScore()
    {
        newScore -= 1;
        NewScore.text = newScore.ToString();
        Debug.Log(newScore);
    }
}
