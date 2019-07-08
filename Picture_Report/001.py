from os import listdir

html_head = r"""
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style type="text/css">
    * {box-sizing: border-box;}
    .row .col {
        width: 12%;
        background-color: #0f0;
        border: 10px solid #fff;
    }
    h1 {
        font-size: 30pt;
        text-align:center;
    }
    h2 {
        text-align:center;
    }
    body {
        background-color: #E6E6D6;
    }
</style>
<script type="text/javascript">
function openShutManager(oSourceObj,oTargetObj,shutAble,oOpenTip,oShutTip){
    var sourceObj = typeof oSourceObj == "string" ? document.getElementById(oSourceObj) : oSourceObj;
    var targetObj = typeof oTargetObj == "string" ? document.getElementById(oTargetObj) : oTargetObj;
    var openTip = oOpenTip || "";
    var shutTip = oShutTip || "";
    if(targetObj.style.display!="none"){
       if(shutAble) return;
       targetObj.style.display="none";
       if(openTip  &&  shutTip){
        sourceObj.innerHTML = shutTip; 
       }
    } else {
       targetObj.style.display="block";
       if(openTip  &&  shutTip){
        sourceObj.innerHTML = openTip; 
       }
    }
}
</script>
<title>Test Report</title>
</head>"""

html_body = r"""
<body>
<h1>Android Automated Test Report</h1>
"""

folders = listdir("step_screenshot")
folders.sort()
for folder in folders:
    reportLink = """
    <h2><a href="###" onclick="openShutManager(this,'%s')">%s</a></h2>
    <p class="row" id="%s" style="display:none">
    """%(folder,folder,folder)
    html_body += reportLink

    Images = listdir("step_screenshot/" + folder)
    Images.sort()
    for ImagePath in Images:
        Image = """
        <img class="col" src="step_screenshot/%s/%s">
        """%(folder,ImagePath)
        html_body += Image
    html_body += "</p>"

def main():
    fp=open('api_result.html','w')
    fp.write(html_head)
    fp.write(html_body)
    fp.close()
    pass

if __name__ == "__main__":
    main()