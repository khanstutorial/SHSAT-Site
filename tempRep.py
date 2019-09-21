#! python3
import re

schedDict = {
    "AST" : '''
                    <section id="schedule" class="special">
                        <header class="major">
                            <h2>KT Astoria</h2>
                            <p></p>
                        </header>
                            <center>
                            <table class="6u 12u$(small)">
                                <tr><th>Sunday</th><td>10am - 2:30pm</td></tr>
                                <tr><th>Monday</th><td>Closed</td></tr>
                                <tr><th>Tuesday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Wednesday</th><td>Closed</td></tr>
                                <tr><th>Thursday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Friday</th><td>4pm - 6pm</td></tr>
                                <tr><th>Saturday</th><td>10am - 2:30pm</td></tr>
                            </table>
                        </center>
                    </section>

        ''',
    "BK" : '''
                    <section id="schedule" class="special">
                        <header class="major">
                            <h2>KT Brooklyn</h2>
                            <p></p>
                        </header>
                            <center>
                            <table class="6u 12u$(small)">
                                <tr><th>Sunday</th><td>10am - 12pm / 12:30pm - 2:30pm</td></tr>
                                <tr><th>Monday</th><td>Closed</td></tr>
                                <tr><th>Tuesday</th><td>Closed</td></tr>
                                <tr><th>Wednesday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Thursday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Friday</th><td>3pm - 5pm</td></tr>
                                <tr><th>Saturday</th><td>10am - 12pm / 12:30pm - 2:30pm</td></tr>
                            </table>
                        </center>
                    </section>

        ''',
    "FP" : '''
                    <section id="schedule" class="special">
                        <header class="major">
                            <h2>KT Floral Park</h2>
                            <p></p>
                        </header>
                            <center>
                            <table class="6u 12u$(small)">
                                <tr><th>Sunday</th><td>10am - 12pm / 12:20pm - 2:30pm</td></tr>
                                <tr><th>Monday</th><td>Closed</td></tr>
                                <tr><th>Tuesday</th><td>10am - 12pm</td></tr>
                                <tr><th>Wednesday</th><td>10am - 12pm</td></tr>
                                <tr><th>Thursday</th><td>Closed</td></tr>
                                <tr><th>Friday</th><td>10am - 12pm</td></tr>
                                <tr><th>Saturday</th><td>10am - 2:30pm</td></tr>
                            </table>
                        </center>
                    </section>

        ''',
    "JA" : '''
                    <section id="schedule" class="special">
                        <header class="major">
                            <h2>KT Jamaica</h2>
                            <p></p>
                        </header>
                            <center>
                            <table class="6u 12u$(small)">
                                <tr><th>Sunday</th><td>12pm - 3pm</td></tr>
                                <tr><th>Monday</th><td>Closed</td></tr>
                                <tr><th>Tuesday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Wednesday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Thursday</th><td>Closed</td></tr>
                                <tr><th>Friday</th><td>4pm - 6pm</td></tr>
                                <tr><th>Saturday</th><td>12pm - 3pm</td></tr>
                            </table>
                        </center>
                    </section>

        ''',
    "JH" : '''
                    <section id="schedule" class="special">
                        <header class="major">
                            <h2>KT Jackson Heights</h2>
                            <p></p>
                        </header>
                            <center>
                            <table class="6u 12u$(small)">
                                <tr><th>Sunday</th><td>10am - 12pm / 12:30pm - 2:30pm</td></tr>
                                <tr><th>Monday</th><td>Closed</td></tr>
                                <tr><th>Tuesday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Wednesday</th><td>Closed</td></tr>
                                <tr><th>Thursday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Friday</th><td>Closed</td></tr>
                                <tr><th>Saturday</th><td>10am - 12pm / 12:30pm - 2:30pm</td></tr>
                            </table>
                        </center>
                    </section>

                    ''',
    "OP" : '''
                    <section id="schedule" class="special">
                        <header class="major">
                            <h2>KT Ozone Park</h2>
                            <p></p>
                        </header>
                            <center>
                            <table class="6u 12u$(small)">
                                <tr><th>Sunday</th><td>10am - 2:30pm</td></tr>
                                <tr><th>Monday</th><td>Closed</td></tr>
                                <tr><th>Tuesday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Wednesday</th><td>Closed</td></tr>
                                <tr><th>Thursday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Friday</th><td>5pm - 7pm</td></tr>
                                <tr><th>Saturday</th><td>10am - 2:30pm</td></tr>
                            </table>
                        </center>
                    </section>

                    ''',
    "PCCH" : '''
                    <section id="schedule" class="special">
                        <center>
                        <div class="6u 12u$(small)">
                        <header class="major">
                            <h2>KT Castle Hill</h2>
                            <p></p>
                        </header>
                            <center>
                            <table>
                                <tr><th>Sunday</th><td>10am - 12pm / 12:30pm - 2:30pm</td></tr>
                                <tr><th>Monday</th><td>Closed</td></tr>
                                <tr><th>Tuesday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Wednesday</th><td>Closed</td></tr>
                                <tr><th>Thursday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Friday</th><td>5pm - 7pm</td></tr>
                                <tr><th>Saturday</th><td>10am - 12pm / 12:30pm - 2:30pm</td></tr>
                            </table>
                        </center>
                    </div>
                    <div class="6u 12u$(small)">
                    <header class="major">
                        <h2>KT Parkchester</h2>
                        <p></p>
                    </header>
                        <center>
                        <table>
                            <tr><th>Sunday</th><td>10am - 12pm / 12:30pm - 2:30pm</td></tr>
                            <tr><th>Monday</th><td>Closed</td></tr>
                            <tr><th>Tuesday</th><td>Closed</td></tr>
                            <tr><th>Wednesday</th><td>12pm - 2pm</td></tr>
                            <tr><th>Thursday</th><td>12pm - 2pm</td></tr>
                            <tr><th>Friday</th><td>5pm - 5pm</td></tr>
                            <tr><th>Saturday</th><td>10am - 12pm / 12:30pm - 2:30pm</td></tr>
                        </table>
                    </center>
                </div>
            </center>
                    </section>

                    ''',
    "RH" : '''
                    <section id="schedule" class="special">
                        <header class="major">
                            <h2>KT Richmond Hill</h2>
                            <p></p>
                        </header>
                            <center>
                            <table class="6u 12u$(small)">
                                <tr><th>Sunday</th><td>10am - 2:30pm</td></tr>
                                <tr><th>Monday</th><td>Closed</td></tr>
                                <tr><th>Tuesday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Wednesday</th><td>Closed</td></tr>
                                <tr><th>Thursday</th><td>12pm - 2pm</td></tr>
                                <tr><th>Friday</th><td>4pm - 6pm</td></tr>
                                <tr><th>Saturday</th><td>10am - 2:30pm</td></tr>
                            </table>
                        </center>
                    </section>

                    ''',
    "SS" : '''
                    <section id="schedule" class="special">
                        <header class="major">
                            <h2>KT Sunnyside</h2>
                            <p></p>
                        </header>
                            <center>
                            <table class="6u 12u$(small)">
                                <tr><th>Sunday</th><td>10am - 12pm / 12:30pm - 2:30pm</td></tr>
                                <tr><th>Monday</th><td>Closed</td></tr>
                                <tr><th>Tuesday</th><td>Closed</td></tr>
                                <tr><th>Wednesday</th><td>Closed</td></tr>
                                <tr><th>Thursday</th><td>Closed</td></tr>
                                <tr><th>Friday</th><td>5pm - 7pm</td></tr>
                                <tr><th>Saturday</th><td>10am - 12pm / 12:30pm - 2:30pm</td></tr>
                            </table>
                        </center>
                    </section>

                    ''',
    "SUT" : '''
                    <section id="schedule" class="special">
                        <header class="major">
                            <h2>KT Astoria</h2>
                            <p></p>
                        </header>
                            <center>
                            <table class="6u 12u$(small)">
                                <tr><th>Sunday</th><td>9:45am - 3pm</td></tr>
                                <tr><th>Monday</th><td>Closed</td></tr>
                                <tr><th>Tuesday</th><td>Closed</td></tr>
                                <tr><th>Wednesday</th><td>4:45pm - 7:30pm</td></tr>
                                <tr><th>Thursday</th><td>Closed</td></tr>
                                <tr><th>Friday</th><td>3:45pm - 6:30pm</td></tr>
                                <tr><th>Saturday</th><td>9:45am - 3pm</td></tr>
                            </table>
                        </center>
                    </section>

                    '''
}

def writeTo(fileName,fileContent):
    with open(fileName,"w+") as outfile:
        outfile.write(fileContent)
    return

def makeFile(branch):
    #schedTarget = "<div id=\"sched\"></div>"
    #schedule = schedDict[branch]

    with open("./index.html","r",encoding='ascii',errors='surrogateescape') as reference:
        refContent = reference.read()
        #startIndex = [m.start() for m in re.finditer(schedTarget, refContent)]
        #lookLen = len(schedTarget)
        #endContent = refContent[:startIndex[0]]+schedule+refContent[(startIndex[0]+lookLen):]
        return refContent
    return endContent

def generateBranch(branch):
    fileName = "index"+branch+".html"
    writeTo(fileName,makeFile(branch))
    return

def branchGeneration():
    branches = ["AST","BK","FP","JA","JH","OP","PCCH","RH","SS","SUT"]

    for x in branches:
        generateBranch(x)
    return

def test():
    generateBranch("AST")
    return

#test()
branchGeneration()
