using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class LivesUpdate : MonoBehaviour {

    public Text LivesRemaining;
    public static int lives;
    private void Start()
    {
        lives = 9;
    }
    
    

    public void DecreaseLives()
    {
        lives -= 1;
        LivesRemaining.text = lives.ToString();
        Debug.Log(lives);
    }

    public void IncreaseLives()
    {
        lives += 1;
        LivesRemaining.text = lives.ToString();
        Debug.Log(lives);
    }

}
