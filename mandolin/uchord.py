# The MIT License (MIT)
#
# Copyright (c) 2017 G. Völkl
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class Chord:
    """

    """

    def __init__(self, name, frets, starting_fret=-1, fingers="", subtexts=""):
        self.name = name
        self.frets = frets
        self.fingers = fingers
        self.subtexts = subtexts
        self.starting_fret = self._calculate_starting_fret(starting_fret, self.frets)

    def _calculate_starting_fret(self,starting_fret,frets):

        if starting_fret != -1:
            return starting_fret

        max_fret = -1
        num_visible_frets = 5

        for i in range(4):
            max_fret = max(max_fret,int(frets[i]))

        if max_fret <= num_visible_frets:
            return 1
        else:
            return max_fret - num_visible_frets + 1

    def to_svg(self):
        """

        :rtype: str
        """
        return """
        <svg width="84" height="124" viewBox="0 0 84 144" style="font-family: sans-serif; font-size: 11px;" 
           xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        """ + self._to_svg() + "</svg>"

    def _to_svg(self):
        closed_string_visible = []
        open_string_visible = []
        fret_y = []
        finger = []
        subtext = []

        for i in range(4):
            if int(self.frets[i]) > 0:
                closed_string_visible.append("visible")
                open_string_visible.append("hidden")
            else:
                closed_string_visible.append("hidden")
                open_string_visible.append("visible")

            fret = int(self.frets[i])
            if self.starting_fret != 1:
                fret = fret - self.starting_fret + 1
            fret_y.append((fret - 1) * 20)
            if self.fingers != "":
                if self.fingers[i] != "_":
                    finger.append(self.fingers[i])
                else:
                    finger.append("")
            else:
                finger.append("")

            if self.subtexts != "":
                if self.subtexts[i] != "_":
                    subtext.append(self.subtexts[i])
                else:
                    subtext.append("")
            else:
                subtext.append("")

        if self.starting_fret != 1:
            starting_fret_visible = "visible"
        else:
            starting_fret_visible = "hidden"

      #<text id="chordName" x="42" y="12" text-anchor="middle" style="font-size: 16px;">{name}</text>
        svg = """
      <text id="startingFret" x="0" y="40" style="visibility: {starting_fret_visible};">{starting_fret}</text>
      <g id="svgChord" transform="translate(9,24)">
        <g id="strings" transform="translate(0,2)">
          <rect height="100" width="2" x="0" fill="black"></rect>
          <rect height="100" width="2" x="20" fill="black"></rect>
          <rect height="100" width="2" x="40" fill="black"></rect>
          <rect height="100" width="2" x="60" fill="black"></rect>
        </g>
        <g id="frets" transform="translate(0,2)">
          <rect height="2" width="62" y="0" fill="black"></rect>
          <rect height="2" width="62" y="20" fill="black"></rect>
          <rect height="2" width="62" y="40" fill="black"></rect>
          <rect height="2" width="62" y="60" fill="black"></rect>
          <rect height="2" width="62" y="80" fill="black"></rect>
          <rect height="2" width="62" y="100" fill="black"></rect>
        </g>
        <g id="closedStrings" transform="translate(1,12)">
          <g id="closedString0" transform="translate(0,{fret_y[0]})" style="visibility: {closed_string_visible[0]};">
            <circle r="6"></circle>
            <text fill="white" id="finger0" y="4" text-anchor="middle" >{finger[0]}</text>
          </g>
          <g id="closedString1" transform="translate(20,{fret_y[1]})" style="visibility: {closed_string_visible[1]};">
            <circle r="6"></circle>
            <text fill="white" id="finger1" y="4" text-anchor="middle">{finger[1]}</text>
          </g>
          <g id="closedString2" transform="translate(40,{fret_y[2]})" style="visibility: {closed_string_visible[2]};">
            <circle r="6"></circle>
            <text fill="white" id="finger2" y="4" text-anchor="middle">{finger[2]}</text>
          </g>
          <g id="closedString3" transform="translate(60,{fret_y[3]})" style="visibility: {closed_string_visible[3]};">
            <circle r="6"></circle>
            <text fill="white" id="finger3" y="4" text-anchor="middle">{finger[3]}</text>
          </g>
        </g>
        <g id="openStrings" transform="translate(1,-5)">
          <circle id="openString0" cx="0" r="4" fill="none" stroke="black" stroke-width="1" style="visibility: {open_string_visible[0]};"></circle>
          <circle id="openString1" cx="20" r="4" fill="none" stroke="black" stroke-width="1" style="visibility: {open_string_visible[1]};"></circle>
          <circle id="openString2" cx="40" r="4" fill="none" stroke="black" stroke-width="1" style="visibility: {open_string_visible[2]};"></circle>
          <circle id="openString3" cx="60" r="4" fill="none" stroke="black" stroke-width="1" style="visibility: {open_string_visible[3]};"></circle>
        </g>
        <g id="subText" transform="translate(1,98)">
          <text id="subText0" x="0" text-anchor="middle">{subtext[0]}</text>
          <text id="subText1" x="20" text-anchor="middle">{subtext[1]}</text>
          <text id="subText2" x="40" text-anchor="middle">{subtext[2]}</text>
          <text id="subText3" x="60" text-anchor="middle">{subtext[3]}</text>
        </g>
      </g>
        """.format(name=self.name,
                   open_string_visible=open_string_visible,
                   starting_fret_visible=starting_fret_visible,
                   starting_fret=self.starting_fret,
                   closed_string_visible=closed_string_visible,
                   fret_y=fret_y,
                   finger=finger, subtext=subtext)
        return svg


class Chords:
    def __init__(self, chordlist):
        self._chordlist = chordlist

    def to_svg(self):
        result = f"""<svg width="{len(self._chordlist)*84}" height="132" style="font-family: sans-serif; font-size: 11px;" 
                 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        """
        for i in range(len(self._chordlist)):
            result += f'<g transform="translate({i * 100},24)">'
            result += self._chordlist[i]._to_svg()
            result += '</g>'
        result += "</svg>"
        return result


def write_chord(filename, name, frets, starting_fret=-1, fingers="", subtexts=""):
    """
    Convenient way to write an svg file
    :param filename: name of svg file
    :param name: chord name
    :param frets: fret positions
    :param starting_fret: number of starting fret
    :param fingers: position of fingers
    :param subtexts: text under the chord
    :return:
    """

    with open(filename, 'w') as f:
        f.write(Chord(name, frets, starting_fret, fingers, subtexts).to_svg())


write_chord('chords/c.svg','','0230',fingers='    ')
write_chord('chords/d.svg','','2002',fingers='    ')
write_chord('chords/e.svg','','1224',fingers='   O')
write_chord('chords/f.svg','','5301',fingers='    ')
write_chord('chords/g.svg','','0023',fingers='    ')
write_chord('chords/a.svg','','2240',fingers='  O ')
write_chord('chords/b.svg','','4122',fingers='    ')
write_chord('chords/cs.svg','','6344',fingers='    ')
write_chord('chords/ds.svg','','0113',fingers='    ') 
write_chord('chords/fs.svg','','3446',fingers='    ')
write_chord('chords/gs.svg','','1134',fingers='    ')
write_chord('chords/as.svg','','3011',fingers='    ')

write_chord('chords/cm.svg','','0134',fingers='    ')
write_chord('chords/dm.svg','','2001',fingers='    ')
write_chord('chords/em.svg','','0220',fingers='    ')
write_chord('chords/fm.svg','','1334',fingers='    ')
write_chord('chords/gm.svg','','0013',fingers='    ')
write_chord('chords/am.svg','','2230',fingers='    ')
write_chord('chords/bm.svg','','4022',fingers='    ')
write_chord('chords/csm.svg','','1240',fingers='    ')
write_chord('chords/dsm.svg','','3112',fingers='    ')
write_chord('chords/fsm.svg','','2445',fingers='    ')
write_chord('chords/gsm.svg','','1124',fingers='    ')
write_chord('chords/asm.svg','','3341',fingers='    ')

write_chord('chords/xmaj-1.svg','','1134',fingers='R  R')
write_chord('chords/xmaj-2.svg','','3113',fingers=' R  ')
write_chord('chords/xmin-1.svg','','1124',fingers='R  R')
write_chord('chords/xmin-2.svg','','3112',fingers=' R  ')
write_chord('chords/x7-1.svg','','1132',fingers='R   ')
write_chord('chords/x7-2.svg','','3142',fingers=' R  ')
write_chord('chords/xm7-1.svg','','1122',fingers='R   ')
write_chord('chords/xm7-2.svg','','3153',fingers=' R  ')

write_chord('chords/xmaj7.svg','','1133',fingers='R   ')
write_chord('chords/x6.svg','','1131',fingers='R   ')
write_chord('chords/xdim.svg','','2135',fingers='R   ')
write_chord('chords/xaug.svg','','1234',fingers='R  R')
