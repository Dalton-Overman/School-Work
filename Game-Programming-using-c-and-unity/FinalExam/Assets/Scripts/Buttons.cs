using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Buttons : MonoBehaviour {

    public void LoadMenu()
    {
        SceneManager.LoadScene("1Intro");
    }

    public void LoadNameEntry()
    {
        SceneManager.LoadScene("2HighScores");
    }

    public void LoadMain()
    {
        SceneManager.LoadScene("3Game");
    }

    public void LoadEnd()
    {
        SceneManager.LoadScene("4Exit");
    }

    public void QuitGame()
    {
        UnityEditor.EditorApplication.isPlaying = false;
        Application.Quit();
    }
        
}
