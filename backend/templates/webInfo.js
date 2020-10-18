function get(search) {

}


function createURL() {
    var p1 = "https://factchecktools.googleapis.com/v1alpha1/claims:search?languageCode=en-US&pageSize=3&query=";
    var p2 = "&key=AIzaSyC-PX-31ru9Y3O4RCKOwloQplLgJ2LTCl8";
    
    var res = document.getElementById("variable").value.toLowerCase();
    res = res.replaceAll("#", "%23");
    res = res.replaceAll("^", "%5E");
    res = res.replaceAll("(", "%28");
    res = res.replaceAll(")", "%29");
    res = res.replaceAll("=", "%3D");
    res = res.replaceAll("+", "%2B");
    res = res.replaceAll("[", "%5B");
    res = res.replaceAll("]", "%5D");
    res = res.replaceAll("{", "%7B");
    res = res.replaceAll("}", "%7D");
    res = res.replaceAll("`", "%60");
    res = res.replaceAll(";", "%3B");
    res = res.replaceAll("/", "%2F");
    res = res.replaceAll("\\", "%5C");
    res = res.replaceAll("|", "%7C");
    res = res.replaceAll("?", "%3F");
    res = res.replaceAll(" ", "%20");
    res = p1 + res + p2;
    console.log(res);
    return(res);
}