<p align="center">
  <img src="https://user-images.githubusercontent.com/29525942/159131458-ddc18a9a-9328-4be5-8efe-3ed471da8f53.png"/>
</p>

<h1 align="center">Computer Virus Spread Visualisation Tool</h1>
<h6 align="center">This repository contains my final year univeristy project.</h6>

## About
The Computer Virus Spread Visualisation Tool is designed for users who may want to gain an understanding of how a computer virus *could potentially* spread under specified parameters, such as recovery and propagation rates, IDS/IPS status and amount of offline nodes etc.

## Screenshots
![Screenshot1](https://user-images.githubusercontent.com/29525942/160676660-94e589e8-aea9-4e07-93f9-9fcc4ee7db14.png)
![Screenshot wide with pin](https://user-images.githubusercontent.com/29525942/160676670-ccd56f0e-5f96-4b51-8b86-8705795ed75e.png)

## Technology
The tool is written in python and utilises the following libraries:
- [PyQT5](https://pypi.org/project/PyQt5/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [SciPy](https://scipy.org/)


## Compartmental Models
Compartmental models are common modelling formulas, often applied in the field of epidemiology to model the spread of infectious diseases and virus. These models, though designed for biological viruses, will hopefully help users better understand the impact a computer virus could have, but also highlight how mitigations such as Firewalls and IDS can help slow the spread. 

### Currently Implemented Models:
#### S.I.R 
![SIR](https://user-images.githubusercontent.com/29525942/159133833-18550d4b-14c0-4462-982f-d1213677621f.png)

``` 
Susceptible ⇢ Infected ⇢ Recovered/Protected
```
#### S.I.S 
![SIS](https://user-images.githubusercontent.com/29525942/159133840-aec51437-be4f-4555-b09f-5d7e83e8504c.png)

``` 
Susceptible ⇢ Infected ⇢ Susceptible
```
#### S.I.R.D 
![SIRD](https://user-images.githubusercontent.com/29525942/159133843-fd95ad7f-5760-4dc2-b4d0-6f3522518d6a.png)

``` 
Susceptible ⇢ Infected ⇢ Recovered or Irrecoverable (Deceased)
```
### Possible Future Models:
#### S.E.I.R 
![SEIR](https://user-images.githubusercontent.com/29525942/159133845-1579dce5-7687-4499-8888-698916964d6f.png)

``` 
Susceptible ⇢ Exposed ⇢ Infected ⇢ Recovered
```

## Authors

[Matt Caine](https://github.com/Matt-Caine)

## License

## Acknowledgments
