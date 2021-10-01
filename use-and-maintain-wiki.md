---
title: Wiki usage and maintenance
description: This page describes the correct usage of this Wiki.
published: true
date: 2020-11-25T09:05:38.524Z
tags: 
editor: undefined
---

# Wiki usage and maintenance

As described on the main page, this wiki splits the documentation into the "history and current state of the aSTEP system" and the "history of the project's management and decisions". As such, this is the kind of documentation we expect you to add to this wiki. Of course, you should also update the wiki when changes are made, such as to the aSTEP system or the services.

## Adding and updating content

> NOTE: These guides were written for Wiki.js 2.4.
{.is-info}

Only the wiki administrators have the authority to create or update wiki-pages. All pages you make on this wiki should be *[markdown](https://www.markdownguide.org/getting-started/) pages*, such that they all follow the same styling. The following subsections quickly explains how to create and edit pages, as well as some details about links and assets (images).

### Creating new pages

To create a new page, do the following:

- First, press the "*New Page*" button to the left of the "*Account*" button.
  - This will reveal a menu showing the current folder structure of the wiki-pages.
  - The names of folders to the left and the names of pages to the right *do not* reflect the actual URLs to those folders or pages.
  - Note that the folders themselves can also represent a page (since we have page with sub-pages).
- Second, navigate to and press the folder you want the new page to be located in.
  - The link at the bottom of the menu should change to reflect that choice.
- Third, replace "*new-page*" with whatever URL you want to give the page and press the "Select" (or that alike) button at the bottom.
	- This does not determine the name/title of the page.
  - The link can be changed later.
  - Do not include trailing or leading slahes (`/`) in the URL, else you'll have to fix it by directly modifying the database.
- Fourth, select the "*markdown*" editor and start writing.
	- Remember to save periodically (the editor will close at the first save/create)
  
If you want to change the page settings, press the "*Page*" button at the på of the markdown editor.

> During 2020 fall semester a service documentation standard was suggested to make a uniform and easy way to find out information about each service. This standard can be found [here: StandardServiceExample.](/services/StandardServiceExample) 
{.is-info}

### Editing existing pages

To start editing an existing page, do the following:

- Go to the page you want to edit.
- Press the "*Page Actions*" button to the left of the "*New Page*" and "*Account*" buttons.
- Press the "*Edit*" button in the popup.

You are now in the mardown editor. If you want to change the page settings, press the "*Page*" button at the på of the markdown editor. Do not include trailing or leading slahes (`/`) in the URL, else you'll have to fix it by directly modifying the database. Remember to save.

> If you change the link of the page (from the "*Page*" menu), you should be careful that links on that page or links to that page from other pages do not break.
> Be careful if you change header names. It is possible to link directly to a header name (`/page#header-name`), and these links will break if you change the headers.
{.is-info}


### Absolute and relative links

While it is the reader's responsibility to learn the syntax of markdown, we'd still like to point out some important details about *links*. A link (e.g. [link]()) in markdown is written like:

- `[link text](url)`

A URL can have three forms:

- External: `www.web.site/path/to/page`
- Absolute: `/path/to/wiki/page`
- Relative: `path/to/sub-page/of/current/page`

Note the difference: the external URL starts with a domain-name (`www.web.site`), the absolute URL starts with just a `/`, and the relative URL starts with "*nothing*" (in loss of a better word).

The external link is quite simple and links to some resource outside the aSTEP wiki. The absolute path links to some page on the aSTEP wiki, given its full path. For example, there is a page on this wiki with the absolute URL `/user-interface/charts`.

However, relative URLs are relative to the page they appear on. That is, if we want to link to `/user-interface/charts` from this current page (`/use-and-maintain-wiki`), we'd define a link with an absolute path:

- `[Link to /user-interface/charts from /use-and-maintain-wiki](/user-interface/charts)`

If we instead suppose we were making a link on the page `/user-interface`, we could define a relative link to the subpage as such:

- `[Link to /user-interface/charts from /user-interface](charts)`

A `relative/path` is automatically translated into: `/absolute/parent/path/` + `relative/path`. In this way, you don't have to update links to a page's subpages, in case you move all of them to a different URL (as long as they always have the same path *relative* to each other).

### HTML support in markdown

You can use many (not sure how many) HTML elements such as div, image, span, table, and more in the markdown editor. However, since the pages are statically rendered, dynamic or intaractive elements such as videos will not work.

### Inserting tables
There are a few ways to insert tables into the wiki pages (and the readme of your services). The first way is the simple way those tables looks like the following:
|Element 1| Element 2|
|---|---|
|value 1| value 2|

These are made by using the "|" symbol around each element like so "| Element 1 | Element 2 |
This is then followed by a row "|---|---|" with a new "---|" added on the end for each element. Lastly the values of each column is added like the column headers "|value 1 | value 2| ... |value n |".

This can be bothersome to look at since it doesn't split up the columns by a bar. So an alternative is to use HTML. These tables you have a little more control over and can look like the following.




<div style="overflow-x:auto;">
<table border="4px solid #000" overflow-x="auto" class="a">
  <tr>
    <th>Element 1</th>
    <th>Element 2</th>
    <th>Element 3</th>
    <th>Element 4</th>
  </tr>
  <tr>
    <th>Value 1</th>
    <th>Value 2</th>
  </tr>
</table>
</div>

To create these it is recommended you start with a wrapper which says "< div style="overflow-x:auto;"> {Place table here} <\div>" (without the spaces between "<" and "div" at the start, this is just to make it into text) This wrapper makes it so if the table becomes too big you get a scroll bar on the x-axis.
Inside this wrapper instead of the "{Place table here}" you place your table. This is written like:
< table overflow-x="auto" class="a"> < tr> < th> Element 1< /th> ... < /tr> < /table>
Here each < tr> < /tr> creates a new row, and the < th> elementname < /th> creates an element in the row.

If you want to change how the border looks, the color, the width or the like you can create a style.
This is done like so:
< style>
        table, th, td {border: 3px solid  #000;}
        table {   border-collapse: collapse; }
< /style>


The border can change colors if you change the #000 value to something else, it represents RGB. Likewise the border should be able to be changed from "solid" to "dotted" or something of the like, see options here: 
https://www.w3schools.com/css/css_border.asp

Be aware, if you insert a style, tables made using the first method will also end up looking like defined in the style.

(If you want to just copy a table you can add rows / columns to you can press the edit on this page and just copy the tables above)

### Images on wiki-pages

To display images on a wiki-page, you should upload them to the wiki by first pressing the "*Insert assets*" in the left side of the editor, and then using the "Upload-box" in the top-right corner.

The assets will be uploaded to the currently selected folder in the left side of the screen, so navigate to or create a proper folder before uploading. 

We know that the root folder is somewhat littered right now, but that is why we advice you follow a proper folder structure.

## Good practices

Following are good guidelines to follow in this wiki:
 
- Create exactly one page describing each service
- Pictures that are used in lists like this:
	- [![astep-small-20x20.png](/astep-small-20x20.png) *Should be 20x20 pixels in size*]()
  {.links-list}
- Follow the folder structure and don't litter the folders with assets or pages.
