from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        domainDict = {}

        for val in cpdomains:
            rep, domain = val.split(" ")
            rep = int(rep)
            frag = domain.split(".")
            for i in range(len(frag)):
                domainDict[".".join(frag[i:])] = rep + domainDict.get(".".join(frag[i:]), 0)
        
        output = []
        for domain, count in domainDict.items():
            formatted_str = f"{count} {domain}"
            output.append(formatted_str)
        
        return output

if __name__ == "__main__":
    input1 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    solution = Solution()
    print(f"Input1: {input1}")
    print(f"Output: {solution.subdomainVisits(input1)}")