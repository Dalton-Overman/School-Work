using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MainSceneScript : MonoBehaviour {


    public static int size;
    public static int speed;
    public static float time;
    public Text timer;
    private float elapsedTime;
    public static int gameScore;
    public static int gameLives;
    public GameObject livesUp;
    public GameObject livesDown;
    public GameObject scoreUp;
    public GameObject scoreDown;
    public Text speedText;
    public Text sizeText;

    // Use this for initialization
    void Start ()
    {
        speedText.text = speed.ToString();
        sizeText.text = size.ToString();
	}
	
	// Update is called once per frame
	void Update ()
    {
        elapsedTime += Time.deltaTime;
        timer.text = Mathf.CeilToInt(time - elapsedTime).ToString();
        if (elapsedTime >= time)
            stopGame();
    }

    public void stopGame()
    {
        gameScore = ScoreUpdate.newScore;
        gameLives = LivesUpdate.lives;
        timer.text = "0";
        scoreDown.SetActive(false);
        scoreUp.SetActive(false);
        livesDown.SetActive(false);
        livesUp.SetActive(false);
    }
}
