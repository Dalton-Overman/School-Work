using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class DropDowns : MonoBehaviour {

    public Dropdown size;
    public Dropdown speed;
    public Dropdown time;





	// Update is called once per frame
	void Update () {

        switch (size.value)
        {
            case 1://small
                MainSceneScript.size = 1;
                break;
            case 2://regular
                MainSceneScript.size = 5;
                break;
            case 3://large
                MainSceneScript.size = 10;
                break;
        }

        switch (speed.value)
        {
            case 1://slow
                MainSceneScript.speed = 1;
                break;
            case 2://regular
                MainSceneScript.speed = 5;
                break;
            case 3://fast
                MainSceneScript.speed = 10;
                break;
        }

        switch(time.value)
        {
            case 1://1 minute
                MainSceneScript.time = 1 * 60f;
                break;
            case 2://3 minute
                MainSceneScript.time = 3 * 60f;
                break;
            case 3://1 minute
                MainSceneScript.time = 5 * 60f;
                break;
        }

    }
}
