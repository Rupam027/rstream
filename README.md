# rstream

> **Stream When and Wherever you want**


**rstream** is a audio streaming utility tool made exclusively for linux users . 

You can add all the applications you use for streaming in a simple configuration file **.stream-config**


**Requirements** 

- Pulse Audio 
- Python3  
- Bash 


**Note**

> You need to run **rstream-init** before using rstream . Also , You can add rstream-init into autostart settings of your distribution . 
> Before running the **rstream-init** ,  replace the Source and Sink variable value with your own source and sink name . 
> You can get the System source and sink information using the **pactl list sources** and **pactl list sinks** .  


### Installation guide 

**1. Clone this repostitory** 

``` 
 git clone https://github.com/Rupam027/rstream
```

**2. Run the install script** 

**System Wide**
```
./install
```

**User Installation**

```
./install --user   
```

**3. Run the command**

*rstream <options>*
 
 
 ### Usage
 
 
rstream list        - List  status of all streams . 

rstream start (src-id) (dest-id) - 
Start a Stream

rstream stop (src-id) (dest - id) -  
Stop a Stream


### Uninstallation 

Run the install script again with the following options :

./install --user --uninstall - If installation is done for particular user . 

./install  --uninstall -   If installation is done system wide . 

 
 
 
 
