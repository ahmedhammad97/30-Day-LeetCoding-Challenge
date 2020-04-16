/**
 * @param {string} s
 * @return {boolean}
 */
function checkValidString(s) {
   return recursiveCheck(s, []) 
};


function recursiveCheck(str, stack) {
    for (let i = 0; i < str.length; i++) {
        switch(str[i]) {
            case '(':
                stack.push(str[i]);
                break;
            case ')':
                if (!(stack.pop() === '(')) return false;
                break;
            case '*':
                return callAsteriskOptions(str, i, stack)
            default:
                console.log("invalid character");
        }
    }
    return stack.length === 0
}


function callAsteriskOptions(str, i, stack) {
    return  recursiveCheck('(' + str.slice(i + 1), stack.slice()) ||
            recursiveCheck(')' + str.slice(i + 1), stack.slice()) ||
            recursiveCheck( '' + str.slice(i + 1), stack.slice())
}


/*
    I preferred the recursive approach even though it is not
    efficient, but it makes sense to me the most.

    The function basically adds and pops parenthesis from a stack
    whenever it encounters a one.
    
    When it came across an `asterisk`, it does three recursive calls,
    one for every possible case, if only one of them return true, then
    it returns true as well.
    
    Finally we make sure the stack is empty before returning.
*/