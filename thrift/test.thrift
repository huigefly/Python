service Transmit {
	string sayMsg(1:string msg, 2:string type='int');
	string invoke(1:i32 cmd 2:string token 3:string data)
}
