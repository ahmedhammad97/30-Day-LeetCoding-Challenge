/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let anagramMap = {};

    strs.forEach(str => {
        let sortedStr = str.split('').sort().join('');
        (anagramMap[sortedStr] || (anagramMap[sortedStr] = [])).push(str);
    });

    return Object.values(anagramMap);
};

/*
 * If we break the problem into smaller blocks, the only
 * challenging block would be matching the anagrams, which
 * I did by using a hashmap, that maps the `char-sorted string`
 * to an array of it's anagram.
 * 
 * The rest of the blocks were taken care of by the awesomeness
 * of JS <3.
 */