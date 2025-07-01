# Micro Zine

This is a little CSS helper for making your own one-sheet zines. 

A zine (/zi:n/) is a self-published, non-commercial print-work that is typically produced in small, limited batches.

This stylesheet focuses on producing no-glue 8-page zines out of a single A4 or Letter paper sheet.

Examples (try printing them!):

* [Ukulele](https://zserge.com/zine/ukulele/) - a helper book for all ukulele chords, fretboard map and common chord progressions.
* [Mandolin](https://zserge.com/zine/mandolin) - a book with simple chords, movable chords, scales and other useful things.
* [Irish Whistle](https://zserge.com/zine/tinwhistle) - a book of well-known tunes to practice tin whistle (Irish whistle).
* [Toki Pona](https://zserge.com/zine/tokipona) - a book about minimalist constructed language with a vocabulary of 120 words.
* [Hollow Men](https://zserge.com/zine/hollow-men/) - a poetry book with a Ukrainian translation of T.S. Eliot's ["Hollow Men"](https://allpoetry.com/the-hollow-men).

## How to write a zine?

Include `zine.css` into your HTML and make a `.zine` element with 8 child elements, one for each page. Style the pages as you wish. 

On screen pages would look like individual sheets and in print mode they will be arranged properly on a landscape sheet of paper ready for printing.

Here's a minimal HTML template to start with:

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="zine.css" rel="stylesheet">
  </head>
  <body>
    <main class="zine">
      <article>
        <h1>Header</h1>
      </article>
      <article>
        <p>First page</p>
      </article>
      <article>
        <p>Second page</p>
      </article>
      <article>
        <p>Third page</p>
      </article>
      <article>
        <p>Fourth page</p>
      </article>
      <article>
        <p>Fifth page</p>
      </article>
      <article>
        <p>Sixth page</p>
      </article>
      <article>
        <h1>The end</h1>
      </article>
    </main>
  </body>
</html>

```

You may use helper grids to layout content on each page: `zine.css` provides you with a 21x15 grid on every page and you can use `grid-area: ....` to position and resize your content. [CSS Grids](https://css-tricks.com/snippets/css/complete-guide-grid/) are pretty powerful!

## How to fold it?

Here's a visual instruction on how to cut and fold it:

![zine-howto](/zine-howto.png)

## License

Zine is distributed under MIT license, so feel free to copy it and use in your own works!

Contributions are always welcome, and you if you found it useful - please let me know about your zine creations (<hello@zserge.com>)!
