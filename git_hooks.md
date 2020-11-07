## git hooks

### usage

First of all, __install git hooks by running:__

```bash
.githooks/install
```

... then do some simple change, try to commit
and see what is happening. :) 

### info

git hooks are in the `.githooks` directory

[`post_commit`](https://github.com/sassbalint/sandbox/blob/master/.githooks/post-commit)
is run after commit by git. Our script is trivial, just prints a message.

[`commit-msg`](https://github.com/sassbalint/sandbox/blob/master/.githooks/commit-msg)
is run after you have finished the current commit message.
Our script perform some checks on the format of the message.

[`install`](https://github.com/sassbalint/sandbox/blob/master/.githooks/install)
is __not__ a real git hook, it is a simple `bash` script for making git hooks available for you. 
Why? git hooks must be in the `.git/hooks` directory
which is __not__ part of the repo!
To be able to use hooks in every clone
we store our git hooks in the `.githooks` directory. 
To use them they should be accessible via `.git/hooks`
so we just convert this to a link to `.githooks`.

