// 错误的答案，因为题目要求不能出现重复的pattern，也就是word中的同一个字符不能对应pattern中的多个字符，word中的多个字符也不能对应pattern中
// 的同一个字符。我开始试图创建两个包含26个字母的字符串sw，sp，分别对应word和pattern。每次从word和pattern中取出一个字符，假设为a，b，
// 在sw和sp中查找是否有对应字符，如果都还在或者都不在了，说明a与b对应的pattern还没有被使用或者已经被使用（这里要注意查找返回的结果如果找到了是索引，
// 没找到的话是-1），两种情况都是符合要求的。而只有一个存在一个不存在的情况才是不符合要求的。
// ***但是这种方法就忽略了之前出现的pattern的a，b的对应关系，如果a与b分别在两个pattern中被使用，那么这个方法会将a与b的pattern认为是合理的，
// 但实际上是不合理的，因为就会造成多对一的pattern

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        
        for word in words:
            sw = string.ascii_letters
            sp = string.ascii_letters
            if len(word) == len(pattern):
                for i in range(len(word)):
                    index1 = sw.find(word[i])
                    index2 = sp.find(pattern[i])
                    print(index1,index2)
                    if index1 < 0 and index2 >= 0 or index1 >= 0 and index2 < 0:
                        break
                    else:
                        sw = sw.replace(word[i],'')
                        sp = sp.replace(pattern[i],'')
                        if i == len(word) - 1:
                            result.append(word)
        
        return result

// 那么重点就是要存储所有出现了的pattern组合，并且是不论顺序的二元组，即(a,b) (b,a)要视为同一个pattern。开始我不知道用什么样的数据结构来实现
// 在我准备进行多次判断的时候，突然发现可以用两个数组来实现，每次出现新的pattern，就将pattern的a,b分别存在两个数组中，保证两个的索引是一样的
// 这样就建立了一个pattern。判断一个新的pattern是否合理的话，就在两个数组中查找a，b，如果两个的索引不一样，说明在之前出现的pattern中他们对应了
// 其他的字母，也就是说这个新的pattern的加入会造成多对一的情况，所以不合理。

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        
        for word in words:
            sw = ''
            sp = ''
            if len(word) == len(pattern):
                for i in range(len(word)):
                    index1 = sw.find(word[i])
                    index2 = sp.find(pattern[i])
                    if index1 != index2:
                        break
                    else:
                        sw += word[i]
                        sp += pattern[i]
                        if i == len(word) - 1:
                            result.append(word)
        
        return result
