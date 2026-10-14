class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 strings s and t, return true if the two strings are anagrams of each other
        # else return false 

        # anagram if they containt he same chars, with each char appearing same number of times, order doesnt matter 


        # put each word in a dict, how do we compare 2 dicts idk. 
        # do we use counter here, but i dont think that is allowed 
        #  return true or false depending on counter? but if that not allowed then idk wat tod o. jst loop each word into a dict and compare each key of the dict? 

        if len(s) != len(t):
            return False
            
        trackS, trackT = {}, {}
        
        for c in s:
            trackS[c] = trackS.get(c,0) + 1
        for c in t:
            trackT[c] = trackT.get(c,0) + 1

        return (trackS == trackT)


        


