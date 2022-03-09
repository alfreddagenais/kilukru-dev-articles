class ProcessStatus {
  static STARTED = new ProcessStatus('STARTED', 1);
  static IN_PROGRESS = new ProcessStatus('IN_PROGRESS', 2);
  static FINISHED = new ProcessStatus('FINISHED', 3);
  
  constructor(key, value) {
    this.key = key;
    this.value = value;
    // here you can include more different properties
    Object.freeze(this);
  }
  
  // toString is just an example of some custom logic that can be implemented here
  toString() {
    return `[${this.key}] => ${this.value}`;
  }
}

// Object
console.log(ProcessStatus.STARTED);
console.log(ProcessStatus.IN_PROGRESS);
console.log(ProcessStatus.FINISHED);

// Object.toString()
console.log(ProcessStatus.STARTED.toString());
console.log(ProcessStatus.IN_PROGRESS.toString());
console.log(ProcessStatus.FINISHED.toString());