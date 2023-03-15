# Lazy-Mapper  
CMD version  
  
  
<img src="https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/showcase.PNG" alt="drawing" width="380"/>
<img src="https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/Custom.gif" alt="drawing" width="380"/>


<!-- TABLE OF CONTENTS -->
### Table of Contents
<ul>
<li><a href="#about">About</a></li>
<li><a href="#prerequisites">Prerequisites</a></li>
<li><a href="#usage">Usage</a></li>
<li><a href="#showcase">Showcase</a></li>
</ul>

<br>

<!-- GETTING STARTED -->
## About
### Curent Features
-Generate Long Stream Maps (Square, Circle, Small Square, or Custom Patterns) for any maps  
-You just need to drag the *lazyMapper.py* script to your song folder and double-click it  
-Starts the first note on the first timing point, ends on the last timing point  
-Can double the bpm for slow maps or halve (Check Situational Folder)  
-My custom templates includes WE LUV LAMA in various difficulties (Different spacing levels)

   
### Future Plans
-GUI Version  
-Adding the possibility for breaks (Editor for now, if you need it)  
-Able to adjust to changing BPM maps and more flexible timing points  
-You won't even need to drag the script to the song folder anymore  
-Saves for Custom Templates  
-Possibility for different patterns such as Jumps, Squares, Corners, Bursts, Triplets, or Quadruplets...   
-On-the-fly custom CS, AR, OD, HP (You have to edit that on the Editor or with FunOranger's Osu-Trainer for now)  

<br>   

For those who are in a sigma grindset like khz's, I'll be happy if it helped someone. But it's mostly for myself for now.  

<br>

### Prerequisites

I believe you only need python.

<br>

<!-- USAGE EXAMPLES -->
## Usage 
Download the <a href="https://github.com/GokaGokai/lazyMapper/releases/tag/0.1.0">latest release</a> or download the zip by clicking the green button on the page (Code, scroll up) or clone my repo.  
  
Open Osu!, go to the editor, and choose a map.  
Open Song Folder (File, top left), and copy *lazyMapper.py* inside.  
(Optional) If you want a custom template, drag it as well in here.
   
<img src="https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/guide.PNG" alt="drawing" width="550"/>


Upon double-clicking *lazyMapper.py*, select one of the maps difficulty. (I would mostly look based of the OD personally)   
  
```
----------

lazyMapper

----------
0 - DJ Sharpnel - WE LUV LAMA 2 (-Tynamo) [ForLMS1.0].osu
1 - xi - Wish upon Twin Stars (Chaoslitz) [BASIC].osu
2 - xi - Wish upon Twin Stars (Chaoslitz) [EXHAUST].osu
3 - xi - Wish upon Twin Stars (Chaoslitz) [Gaia's ADVANCED].osu
4 - xi - Wish upon Twin Stars (Chaoslitz) [HYPER].osu
5 - xi - Wish upon Twin Stars (Chaoslitz) [NOVICE].osu
6 - xi - Wish upon Twin Stars (Chaoslitz) [Wish].osu

Which map to parse from? (Only for stats such as CS, AR, OD, HP..)
```
Prompt Example: 6  
<br>   

```
---
0 - Square
1 - Circle
2 - Small Square
3 - Custom

What kind of map do you want to generate?

```
Prompt Example: 3 (The third prompt will only show if you select Custom)  
<br>   

```
---
0 - DJ Sharpnel - WE LUV LAMA 2 (-Tynamo) [ForLMS1.0].osu
1 - xi - Wish upon Twin Stars (Chaoslitz) [BASIC].osu
2 - xi - Wish upon Twin Stars (Chaoslitz) [EXHAUST].osu
3 - xi - Wish upon Twin Stars (Chaoslitz) [Gaia's ADVANCED].osu
4 - xi - Wish upon Twin Stars (Chaoslitz) [HYPER].osu
5 - xi - Wish upon Twin Stars (Chaoslitz) [NOVICE].osu
6 - xi - Wish upon Twin Stars (Chaoslitz) [Wish].osu

Select the osu file you want to copy from (Assuming you dragged it in the same folder already)
```
Prompt Example: 0 (Using the template in my github)  
<br>   

Done! You should be able to see the new map in the folder, which was *xi - Wish upon Twin Stars (Chaoslitz) [lazyMapperCustom (DJ Sharpnel - WE LUV LAMA 2 (-Tynamo) [ForLMS1.0].osu)].osu* in this example.   
Just go back to Osu! and search it. (Refresh it by going in and out of the menu)  

<br>   

(If you have any questions, discord: GokaGokai#7048)

## Showcase
Using *lazyMapper.py* on <a href="https://osu.ppy.sh/beatmapsets/242462#osu/559673">Wish upon Twin Stars</a>

### Square


![](https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/Square.gif)

### Circle


![](https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/Circle.gif)

### Small Square


![](https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/SmallSquare.gif)

### Custom
(Using the template DJ Sharpnel - WE LUV LAMA 2 (-Tynamo) [ForLMS1.0].osu)


![](https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/Custom.gif)
