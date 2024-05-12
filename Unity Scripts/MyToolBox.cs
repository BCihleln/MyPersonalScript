using UnityEngine;
using System;
 
public static class MyToolBox
{
    public static void SetRandom(ref Vector2 Target,float[] RangeX, float[] RangeY)
    {
        Target.Set(UnityEngine.Random.Range(RangeX[0],RangeX[1]),UnityEngine.Random.Range(RangeY[0],RangeY[1]));
    }
    public static void SetRandom(ref Vector3 Target,float[] RangeX, float[] RangeY,float[] RangeZ)
    {
        Target.Set(UnityEngine.Random.Range(RangeX[0],RangeX[1]),UnityEngine.Random.Range(RangeY[0],RangeY[1]),UnityEngine.Random.Range(RangeZ[0],RangeZ[1]));
    }

    // public delegate void Func(); //C#委托Delegate，可用C/C++函數指針理解
    public static void CountDown(ref float ObjectCounter, ref float CounterMax, Action CountEndAction)
    {
        // delegate,Action,Func Has the posibilty to cause Memory Leak
        if(ObjectCounter < CounterMax) ObjectCounter+=Time.deltaTime;
        else {CountEndAction();ObjectCounter = 0f;}
    }
}