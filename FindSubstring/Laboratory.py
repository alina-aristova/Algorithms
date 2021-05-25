import numpy as np

class Laboratory:
    def getAlphabet(self, substring):
        alphabet = list()
        for i in substring:
            if i not in alphabet:
                alphabet.append(i)
        return alphabet

    def getSuffixTable_Automat(self, substring):
        substr = [substring[0]]
        alphabet = self.getAlphabet(substring)
        table = np.zeros((len(substring) + 1, len(alphabet)), dtype=np.int)
        for indexP, valueP in enumerate(substring):
            if indexP != 0:
                substr.append(substr[-1] + valueP)
            for idx, val in enumerate(alphabet):
                if indexP == 0:
                    if valueP == val:
                        table[indexP][idx] = 1
                else:
                    substr_ = substr[-2] + val
                    table[indexP][idx] = self.prefix(substr[-1] + '|' + substr_)[-1]
                    if indexP == len(substring) - 1:
                        table[indexP + 1][idx] = self.prefix(substr[-1] + '|' + substr[-1] + val)[-1]
        return table

    def prefix(self, line):
        k = 0
        strLength = len(line)
        pi = [0] * strLength
        pi[0] = k
        for i in range(1, strLength):
            k = pi[i - 1]
            while k > 0 and line[k] != line[i]:
                k = pi[k - 1]
            if line[k] == line[i]:
                k += 1
            pi[i] = k
        return pi

    def kmp(self, text, substring):
        
        p = substring + '#'+ text
        
        pi = self.prefix(p)
        k = 0
        result = list()
        for i in range(1, len(text)):
            while k > 0 and substring[k] != text[i]:
                k = pi[k - 1]
            if substring[k] == text[i]:
                k = k + 1
            if k ==len(substring):
                result.append(i-len(substring)+1)
                k = pi[k - 1]
        return result

    def rabin_karp(self,text,substring):
        alphabet = 'abcdifghijklmnopqrstuvwxyz'
        d = len(alphabet)
        q= 2
        n = len(text)
        m =len(substring)
        d_m= d**(m-1)%q
        result = list()
        h=0
        h_=0
        for i in range(0,m-1):
            h = d*h + ord(substring[i])%q
            h_ = d*h + ord(text[i])%q
            for s in range(0,n-m):
                if h == h_:
                    if substring == text[s:s+m]:
                        result.append(s)
                if s < n-m :
                    h_ =( d*(h_-d_m*ord(text[s]))+ord(text[s+m]))%q
        return result
    
    def boera_mura(self, text, substring):
        suff = self.getSuffixTable_BoeraMura(substring)
        stop = self.getStopTable(text,substring)
        result = list()
        for i in range(0,(len(text)-len(substring)+1)):
            j = len(substring) - 1
            while j>=0 and substring[j] == text[i+j]:
                j = j - 1

            if j == -1:
                result.append(i)
                delta_stop = 1
            else:
                delta_stop = j -stop[text[i + j]]
            delta_suff = suff[j+1]
            i = i + max(delta_stop, delta_suff)
        return result

    def getSuffixTable_BoeraMura(self, substring):
        m = len(substring)
        pref = self.prefix(substring)
        revSubstring = substring[::-1]
        pref_  = self.prefix(revSubstring)
        table = [0]*(m+1)
        
        for i in range(0, m+1):#1
            table[i] = m - pref[m-1]
        for i in range(0,m):
            ind = m - pref_[i]
            shift = i - pref_[i] +1
            if table[ind] > shift:
                table[ind] = shift
        return table

    def getStopTable(self, text, substring):
        stopTable = dict()
        for i in range(len(substring)-1):
            stopTable.update({substring[i]:i})
        for k in text:
            if k not in stopTable:

                stopTable.update({k:-1})
        return stopTable
    