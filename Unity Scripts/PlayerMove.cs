using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMove : MonoBehaviour
{
    public float speed;
    public Vector3 playerInput;
    Animator anim;
    float noInputTime;

    // Start is called before the first frame update
    void Start()
    {
        anim = gameObject.GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {

        //设置状态机中的noInput，以触发打盹动画
        if (noInputTime < 5) { noInputTime += Time.deltaTime; }
        anim.SetFloat("noInput", noInputTime);

        //设置状态机中的isRunning，以触发移动和站立动画
        if (playerInput != Vector3.zero)
        {
            anim.SetBool("isRunning", true);
            noInputTime = 0;
        }
        else
        {
            anim.SetBool("isRunning", false);
        }

        //玩家的移动代码
        playerInput = new Vector3(Input.GetAxisRaw("Horizontal"), Input.GetAxisRaw("Vertical"));
        transform.position += (playerInput * speed * Time.deltaTime);

    }
}
