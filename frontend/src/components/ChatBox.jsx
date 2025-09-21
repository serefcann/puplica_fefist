import React from 'react'
import MessageBubble from './MessageBubble'
import TypingIndicator from './TypingIndicator'

const ChatBox = ({ messages, isLoading, messagesEndRef }) => {
  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-gray-50 dark:bg-gray-900 transition-colors duration-200">
      {messages.length === 0 && !isLoading && (
        <div className="flex items-center justify-center h-full">
          <div className="text-center text-gray-500 dark:text-gray-400">
            <div className="text-6xl mb-4">🎓</div>
            <h2 className="text-xl font-medium mb-2 text-gray-700 dark:text-gray-300">YÖK Atlas RAG Chatbot</h2>
            <p className="text-sm">Üniversite ve program bilgileri hakkında sorularınızı sorabilirsiniz.</p>
          </div>
        </div>
      )}
      
      {messages.map((message) => (
        <MessageBubble key={message.id} message={message} />
      ))}
      
      {isLoading && <TypingIndicator />}
      
      <div ref={messagesEndRef} />
    </div>
  )
}

export default ChatBox


