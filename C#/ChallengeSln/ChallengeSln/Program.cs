using System;

namespace ChallengeSln
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
             
            */
        }

        public static string ReplaceVowels(string str, string ch)
        {
            char[] sent = str.ToCharArray();
            for (int i=0; i < sent.Length; i++)
            {
                if(sent[i] == 'a' || sent[i] == 'e' || sent[i] == 'i' || sent[i] == 'o' || sent[i] == 'u')
                {
                    sent[i] = ch[0];
                }
            }
            string final = new string(sent);
            return final;
        }
    }
}
