import React from 'react'

const TypingIndicator = () => {
  return (
    <div className="flex justify-start">
      <div className="flex flex-col max-w-xs lg:max-w-md xl:max-w-lg">
        <div className="bot-message message-bubble">
          <div className="flex items-center space-x-1">
            <span className="text-sm text-gray-600">Yanıt yazıyor</span>
            <div className="flex space-x-1">
              <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce-slow"></div>
              <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce-slow" style={{ animationDelay: '0.1s' }}></div>
              <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce-slow" style={{ animationDelay: '0.2s' }}></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default TypingIndicator

