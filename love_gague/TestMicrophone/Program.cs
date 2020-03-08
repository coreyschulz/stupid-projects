using System;

using NAudio;
using NAudio.Wave;

using System.Threading; 

using VoiceRecorder.Audio; 

namespace TestMicrophone
{
    class Program
    {

        static void Main(string[] args)
        {

            AudioRecorder test = new AudioRecorder();
            test.BeginMonitoring(0);

            double loveGaugeVerageAverage = 0;
            int loveCount = 0;

            while(true)
            {
                double average = test.getLoveGagueAverage();
                loveGaugeVerageAverage += (average - loveGaugeVerageAverage) * 0.05;

                if (test.getLoveGagueAverage() - loveGaugeVerageAverage >= 40)
                {
                    //Console.WriteLine("BCS3 detected your love!! <3");
                    loveCount += 1;
                    if (loveCount >= 100)
                        break;

                    Console.Write("[");
                    for (int i = 0; i < 100; i++)
                        Console.Write(i < loveCount ? "-" : " ");
                    Console.WriteLine("]");
                }
                Thread.Sleep(100); 
            }

            Console.WriteLine("YOU DID IT!!!");



        }



    }
}
