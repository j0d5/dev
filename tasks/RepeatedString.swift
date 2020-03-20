
/// ## Repeated String
func repeatedString(s: String, n: Int) -> Int {
    var string = ""
    while string.count < n {
        string.append(s)
    }
    return string.prefix(n).filter({character -> Bool in character == "a"}).count
}

let s = "aba"
print(repeatedString(s: s, n: 10))