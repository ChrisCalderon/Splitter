from ethereum import tester as t

def run_test():
    s = t.state()
    c = s.abi_contract('splitter.se')
    account = c.new_account()
    c.deposit(account, value=100)
    print s.block.get_balance(t.a1)
    c.withdraw(account, t.a1)
    print s.block.get_balance(t.a1)

if __name__ == '__main__':
    run_test()
