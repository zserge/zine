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
        num_visible_frets = 4

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
        <svg width="84" height="124" viewBox="0 0 84 124" style="font-family: sans-serif; font-size: 11px;" 
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
          <rect height="80" width="2" x="0" fill="black"></rect>
          <rect height="80" width="2" x="20" fill="black"></rect>
          <rect height="80" width="2" x="40" fill="black"></rect>
          <rect height="80" width="2" x="60" fill="black"></rect>
        </g>
        <g id="frets" transform="translate(0,2)">
          <rect height="2" width="62" y="0" fill="black"></rect>
          <rect height="2" width="62" y="20" fill="black"></rect>
          <rect height="2" width="62" y="40" fill="black"></rect>
          <rect height="2" width="62" y="60" fill="black"></rect>
          <rect height="2" width="62" y="80" fill="black"></rect>
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
            result += f'<g transform="translate({i * 80},24)">'
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


write_chord('chords/c.svg','','0003',fingers='0003')
write_chord('chords/d.svg','','2220',fingers='1230')
write_chord('chords/e.svg','','4442',fingers='2341')
write_chord('chords/f.svg','','2010',fingers='2010')
write_chord('chords/g.svg','','0232',fingers='0132')
write_chord('chords/a.svg','','2100',fingers='2100')
write_chord('chords/b.svg','','4322',fingers='3211')
write_chord('chords/cs.svg','','1114',fingers='1114')
write_chord('chords/ds.svg','','0331',fingers='0341')
write_chord('chords/fs.svg','','3121',fingers='3121')
write_chord('chords/gs.svg','','5343',fingers='3121')
write_chord('chords/as.svg','','3211',fingers='3211')

write_chord('chords/cm.svg','','0333',fingers='0111')
write_chord('chords/dm.svg','','2210',fingers='2310')
write_chord('chords/em.svg','','0432',fingers='0321')
write_chord('chords/fm.svg','','1013',fingers='1024')
write_chord('chords/gm.svg','','0231',fingers='0231')
write_chord('chords/am.svg','','2000',fingers='2000')
write_chord('chords/bm.svg','','4222',fingers='3111')
write_chord('chords/csm.svg','','1104',fingers='1204')
write_chord('chords/dsm.svg','','3321',fingers='3421')
write_chord('chords/fsm.svg','','2124',fingers='2134')
write_chord('chords/gsm.svg','','1342',fingers='1342')
write_chord('chords/asm.svg','','3111',fingers='3111')

write_chord('chords/c7.svg','','0001',fingers='0001')
write_chord('chords/d7.svg','','2223',fingers='1112')
write_chord('chords/e7.svg','','1202',fingers='1203')
write_chord('chords/f7.svg','','2313',fingers='2413')
write_chord('chords/g7.svg','','0212',fingers='0213')
write_chord('chords/a7.svg','','0100',fingers='0200')
write_chord('chords/b7.svg','','2322',fingers='1211')
write_chord('chords/cs7.svg','','1112',fingers='1112')
write_chord('chords/ds7.svg','','3334',fingers='1112')
write_chord('chords/fs7.svg','','3424',fingers='2413')
write_chord('chords/gs7.svg','','1323',fingers='1324')
write_chord('chords/as7.svg','','1211',fingers='1211')

write_chord('chords/cm7.svg','','3333',fingers='1111')
write_chord('chords/dm7.svg','','2213',fingers='3214')
write_chord('chords/em7.svg','','0202',fingers='0102')
write_chord('chords/fm7.svg','','1313',fingers='1324')
write_chord('chords/gm7.svg','','0211',fingers='0211')
write_chord('chords/am7.svg','','2433',fingers='1322')
write_chord('chords/bm7.svg','','2222',fingers='1111')
write_chord('chords/csm7.svg','','1102',fingers='1203')
write_chord('chords/dsm7.svg','','3324',fingers='2314')
write_chord('chords/fsm7.svg','','2424',fingers='1324')
write_chord('chords/gsm7.svg','','1322',fingers='1322')
write_chord('chords/asm7.svg','','1111',fingers='1111')

write_chord('chords/xdim.svg','','1212',fingers='   R')
write_chord('chords/xaug.svg','','4332',fingers='R  R')
write_chord('chords/x6.svg','','4646',fingers='R   ')
write_chord('chords/xmaj7.svg','','4666',fingers='R   ')

