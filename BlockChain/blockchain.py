import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []
		self.new_block(previous_hash=1,proof=100)

	def new_block(self,proof, previous_hash = None):
		#创建一个新的区块并把它添加到链
		block = {
		'index': len(self.chain) + 1,
		'timestamp': time(),
		'transactions': self.current_transactions,
		'proof': proof,
		'previous_hash': previous_hash or self.hash(self.chain[-1]),
		}
		self.current_transactions = []
		self.chain.append(block)
		return block

	def new_transaction(self, sender, recipient, amount):
		#添加一条信息到信息列表
		self.current_transactions.append({
			'sender': sender,
			'recipient': recipient,
			'amount': amount,
			})
		return self.last_block['index'] + 1

	@staticmethod
	def hash(block):
		#哈希加密区块
		block_string = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()

	@property
	def last_block(self):
		#返回上一个区块
		return self.chain[-1]

	#寻找一个数字proof使得其和上一个的proof求哈希时，开头均为0000
	def proof_of_work(self, last_proof):
		proof = 0
		while self.vaild_proof(last_proof, proof) is False:
			proof += 1

	@staticmethod
	def vaild_proof(last_proof, proof):
		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()
		return guess_hash[:4] == "0000"

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-','')

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    block = blockchain.new_block(proof)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/transactions/new', methods = ['POST'])
def new_transaction():
	values = request.get_json()
	required = ['sender', 'recipient', 'amount']
	if not all(k in values for k in required):
		return 'Missing values',400

	index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

	response = {'message': f'Transaction will be added to Block {index}'}
	return jsonify(response),201

@app.route('/chain', methods=['GET'])
def full_chain():
	response = {
		'chain': blockchain.chain,
		'length': len(blockchain.chain),
	}
	return jsonify(response),200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

