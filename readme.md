# autogrep - Easy to use log extractor

## Usecases

- Extracting useful information from huge files with ease
- Using grep repeatedly




## Installation

1. Clone the repository:

```bash
git clone https://github.com/izhlb/autogrep.git
```

2. Enter the repo

```bash
cd ./autogrep
```

3. Configure the `settings.json` file


```json
{
    "types":{
        "premade": {
            "test": ["google.com"]
        },
        "custom": {
            
        }    
    },
    "verbose" : "False",
    "filepath": "D:/T",

}
```

## Configuring

The main config file `settings.json` is located the main folder

You can configure the program with your custom link arrays

```json
"types":
{
    "premade": {
        "test": ["google.com", "instagram.com", "facebook.com"]
    },
},

```

### Verbose output

You could enable the verbose output for debugging reasons.

```json
"verbose" : "False",
```




## :white_check_mark: Todo:

- [x] Basic Functionality
- [x] JSON Integration
- [ ] Make it prettier
- [ ] Add indicators on how many hits you've found
- [ ] Make a bash mode switcher

