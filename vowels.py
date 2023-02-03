#include <iostream>
using namespace std;
// to keep the string in lexicographically sorted order use
// start index
// to add the vowels starting the from that index
int countstrings(int n, int start)
{
    // base case: if string length is 0 add to the count
    if (n == 0) {
        return 1;
    }
    int cnt = 0;
    // if last character in string is 'e'
    // add vowels starting from  'e'
    // i.e    'e','i','o','u'
    for (int i = start; i < 5; i++) {
        // decrease the length of string
        cnt += countstrings(n - 1, i);
    }
    return cnt;
}
int countVowelStrings(int n)
{
    //  char arr[5]={'a','e','i','o','u'};
    // starting from index 0 add the vowels to strings
    return countstrings(n, 0);
}
int main()
{
    int n = 2;
    cout << countVowelStrings(n);
    return 0;
