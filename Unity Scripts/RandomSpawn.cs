using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RandomSpawn : MonoBehaviour
{
    public GameObject Target;
    public float SpawnTimeBase,SpawnTimeOffset;
    float counter;
    float SpawnTimeLeast, SpawnTimeMost;

    // Start is called before the first frame update
    void Start()
    {
        SpawnTimeLeast = (SpawnTimeBase - SpawnTimeOffset) > 0 ? SpawnTimeBase - SpawnTimeOffset : 0.1f;
        SpawnTimeMost = SpawnTimeBase + SpawnTimeOffset;
        counter = Random.Range(SpawnTimeLeast, SpawnTimeMost);
    }

    // Update is called once per frame
    void Update()
    {
        if (counter < 0)
        {
            Vector3 position = new Vector3(Random.Range(-5f, 5f), Random.Range(-5f, 5f), Random.Range(-5f, 5f));
            Instantiate(Target, position, Quaternion.identity);
            counter = Random.Range(SpawnTimeLeast, SpawnTimeMost);
        }
        else
        {
            counter -= Time.deltaTime;
        }
    }
}
