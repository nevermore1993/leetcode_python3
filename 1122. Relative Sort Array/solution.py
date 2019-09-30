// 首先构建字典，key为B中的元素，value为对应在B中的索引
// 然后对A进行排序，排序的key是A中的元素在字典中的value，也就是顺序，如果A中的元素不在B中，那么返回1000+a
// 因为按照题目，A，B的长度是在0-1000之间的，加1000就不会与出现了的元素冲突
// 排序的key，就是指定了排序的标准。最原始的排序，我们排序的标准就是数字本身。而当我们需要对更复杂的对象进行排序时，就需要指定
// 对象的某个属性，按照这个属性来将对象进行排序。这个属性就是key。这里的key就是A中元素出现在B中的顺序
def relativeSortArray(self, A, B):
        k = {b: i for i, b in enumerate(B)}
        # k.get(key, default) 返回字典k中键为key的值，如果不存在键key，则返回default
        return sorted(A, key=lambda a: k.get(a, 1000 + a))
        
        
// 这里也是按照索引来排序，sorted(A)是为了处理不在B中的元素的顺序。B+sorted(A)保证了B中的元素排在前面。
def relativeSortArray(self, A, B):
        return sorted(A, key=(B + sorted(A)).index)
