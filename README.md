# Runtime Status Analysis for K8s
Fetch the K8s pods' Runtime status & analysis
![Logo](https://github.com/englandbaron/CadvisorAnalysis/blob/master/Image/logo.png)<br/>
# Introduction
As a container status collector, CAdvisor could provide developer with several features:<br/>
 - Memory/CPU runtime history stats
 - Machine summary

In this project, I've re-format the API Response and provided some powerful Models, it supports:
 - FILE
 ```
 workspace = ProjectWorkspace("FILE","DataSet-Demo/")
 ```
 - HTTP
 ```
 workspace = ProjectWorkspace("HTTP","http://node1:8080"))
 ```

# Installation
Environment: ***Python3/pip***
```bash
pip install -r requirements.txt
```

# Tutorial
```bash
python test.py
```
