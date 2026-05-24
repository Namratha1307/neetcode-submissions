class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for s in strs:
            encoded_string=encoded_string + str(len(s))+"#"+s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result_list=[]
        index=0
        while index<len(s):
            sep_pos=s.find('#', index)
            str_length=int(s[index:sep_pos])
            start_of_str=sep_pos+1
            actual_str=s[start_of_str:start_of_str+str_length]
            result_list.append(actual_str)
            index=start_of_str+str_length
        return result_list