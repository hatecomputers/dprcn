# 🔬 dprcn
dpcrn aka dope recon is a module-oriented recon tool.

* [Why another recon tool]()
* [How it works]()
    * [External modules]()
    * [Understanding modules.json]()
* [Should I use this?]()  

## Why another recon tool

This started as a _refactor_ of my existing [recon-all-things]() script, which was cluttered and unexplicably unflexible. In the process of learning new things and / or having new ideas, I wanted something easy so I could quickly introduce new workflows or modifying the ones which are no longer useful. By creating this, things look a little more managable. Think of it as an orchestrator, if you will.

## How it works 

This is a module-oriented tool, which means it relies on two things: 
* external modules 
* a config file which dictates how those modules interact with one another (modules.json)

### External modules

This can be pretty much anything. 

### Understanding modules.json

The __modules.json__ file is used to describe a series of actions which when put together, result in a workflow as presented below:

```json
{
    "setup":  {
        "should_run": "True",
        "modules":[
            {
                "description": "Initial setup",
                "should_run": true, 
                "instructions": [
                  "rm -rf {directory}",
                  "mkdir -p {directory}"
                ]
            }
    ]},
    "subdomains": {
        "should_run": true,
        "modules":[
            {
              "description": "Extract subdomains from crt.sh",
              "should_run": true, 
              "instructions": [
                  "curl -s https://crt.sh/?q=%25.{domain}\\&output=json",
                  "jq -r '.[].name_value'",
                  "grep -v '*' >> {directory}/domains/crtsh.subdomains"
                ]
            }
    ]}
    ...
```

Notice that both `{domain}` and `{directory}` are reserved words that get replaced by the actual values in runtime. 

## Should I use this?

Probably not. However, I would love to see some contributions. At the beginning, this was meant to be exclusive personal toy because I enjoy writing my own tools and adapt it to my very own needs. If, for whatever reason, you decide to give a go but think it sucks, feel free to fork it or replace it entirely for something better and let me know. I gladly use your version instead :)


