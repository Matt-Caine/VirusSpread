<p align="center">
  <img src="https://user-images.githubusercontent.com/29525942/159131458-ddc18a9a-9328-4be5-8efe-3ed471da8f53.png"/>
</p>

<h1 align="center">Computer Virus Spread Visualisation Tool</h1>
<h6 align="center">This repository is for my final year univeristy project.</h6>

## About
The Computer Virus Spread Visualisation Tool is designed for users who may want to gain an understanding of how a computer virus *could potentially* spread under specified parameters, such as recovery and propagation rates, IDS/IPS status and amount of offline nodes etc.
## Installation
1. Download latest release by clicking [here](https://github.com/Matt-Caine/VirusSpread/releases/download/v0.1/Computer.Virus.Spread.Visualisation.Tool.zip)
2. Extract contents.
3. Run "main.exe" within the extracted file. Create a desktop shortcut if desired. 

## Screenshots
![Main Window](https://user-images.githubusercontent.com/29525942/162276730-a61503e1-e679-4b06-b8ac-2804e0483eba.png)
![Main Window With Comparison Window Open](https://user-images.githubusercontent.com/29525942/162276776-d89850b5-2ec6-4757-9a3e-2cc5059efecb.png)

<h6 align="center">Screenshots show the Main Window and the Main Window With Comparison Mode Open</h6>

## Compartmental Models
Compartmental models are common modelling formulas, often applied in the field of epidemiology to model the spread of infectious diseases and virus. These models, though designed for biological viruses, will hopefully help users better understand the impact a computer virus could have, but also highlight how mitigations such as Firewalls and IDS can help slow the spread. 

### Currently Implemented Models:

| S.I.R  | S.I.S  | S.I.R.D  |
| :---:  | :---:  |   :---:  |
| ![SIR](https://user-images.githubusercontent.com/29525942/159133833-18550d4b-14c0-4462-982f-d1213677621f.png)  | ![SIS](https://user-images.githubusercontent.com/29525942/159133840-aec51437-be4f-4555-b09f-5d7e83e8504c.png)  | ![SIRD](https://user-images.githubusercontent.com/29525942/159133843-fd95ad7f-5760-4dc2-b4d0-6f3522518d6a.png)  |
  
## Technology/Acknowledgments
The tool is written in python and utilises the following libraries:
- [PyQT5](https://pypi.org/project/PyQt5/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [SciPy](https://scipy.org/)

## Miscellaneous
### Colour Palette
![Colours](https://user-images.githubusercontent.com/29525942/161639343-1886b24c-5a7c-43fa-958c-eca680eb30ed.png)

## Authors

[Matt Caine](https://github.com/Matt-Caine)
- [Website](https://matt-caine.github.io/)
- [Twitter](https://twitter.com/MattCaine_)

